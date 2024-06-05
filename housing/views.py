from io import BytesIO

import pandas as pd

from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from accreditations.models import Accreditation
from core.views import AccreditationViewSet
from core.utils import split_space
from countries.models import Country

from housing.models import Housing, HousingPerson
from housing.serializers import HousingSerializer, HousingPersonSerializer


def is_same_housing(housing: Housing, data) -> bool:
    same_house = data['address'] == housing.address and \
                 data['house_number'] == housing.house_number

    same_apartment = data['address'] == housing.address and \
                     data['apartment_tower'] == housing.apartment_tower and \
                     data['apartment_number'] == housing.apartment_number

    return same_house or same_apartment


class HousingViewSet(AccreditationViewSet):
    queryset = Housing.objects.all()
    serializer_class = HousingSerializer
    filterset_fields = ['status']
    search_fields = [
        'persons__first_name',
        'persons__last_name',
        'created_at__date',
    ]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.times_edited == 0:
            instance.times_edited += 1
            instance.save()

        return super().update(request, *args, **kwargs)

    @action(detail=False,
            methods=['get'],
            permission_classes=[AllowAny])
    def export(self, request, *args, **kwargs) -> HttpResponse:
        queryset = Housing.objects \
            .filter(status=Accreditation.Status.PENDING) \
            .prefetch_related('persons', 'persons__country')

        if not queryset.exists():
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)

        buffer = BytesIO()

        values = []

        for housing in queryset:
            for person in housing.persons.all():
                values.append({
                    'ID': person.id,
                    'Primer Nombre': split_space(person.first_name)[0],
                    'Segundo Nombre': split_space(person.first_name)[1],
                    'Primer Apellido': split_space(person.last_name)[0],
                    'Segundo Apellido': split_space(person.last_name)[1],
                    'Cédula': person.passport_id,
                    'Fecha de Nacimiento': person.birthday.strftime('%d-%m-%Y'),
                    'Nacionalidad': person.country.nationality
                })

        pd.DataFrame(values).to_excel(
            buffer, index=False, sheet_name='Personas')
        buffer.seek(0)

        response = HttpResponse(
            buffer.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        )

        response['Content-Disposition'] = 'attachment; filename=data.xlsx'

        return response

    @action(detail=False,
            methods=['post'],
            url_path='import', url_name='import',
            permission_classes=[AllowAny])
    def import_data(self, request: Request, *args, **kwargs) -> Response:
        try:
            df_housings = pd.read_excel(request.FILES['data'], sheet_name='Residentes')
            df_housings = df_housings.rename(columns={
                'Dirección': 'address',
                'Tipo de Edificio': 'building_type',
                'Número de Casa': 'house_number',
                'Torre de Apartamento': 'apartment_tower',
                'Nombre de Administrador': 'building_admin_name',
                'Número de Apartamento': 'apartment_number',
                'Piso de Apartamento': 'apartment_floor',
                'Es Propietario': 'is_owner',
                'Nombre del Propietario': 'owner_name',
                'Teléfono del Propietario': 'owner_phone_number',
            })

            df_housings['building_type'] = df_housings['building_type'] \
                .apply(lambda label: 'HOUSE' if label == 'Casa' else 'APARTMENT')

            df_housings['is_owner'] = df_housings['is_owner'].apply(lambda label: label == 'Sí')

            df_housings['house_number'] = df_housings['house_number'].fillna('')
            df_housings['apartment_tower'] = df_housings['apartment_tower'].fillna('')
            df_housings['apartment_number'] = df_housings['apartment_number'].fillna('')
            df_housings['apartment_floor'] = df_housings['apartment_floor'].fillna('')
            df_housings['owner_name'] = df_housings['owner_name'].fillna('')
            df_housings['owner_phone_number'] = df_housings['owner_phone_number'].fillna('')
            df_housings['building_admin_name'] = df_housings['building_admin_name'].fillna('')

        except KeyError:
            return Response(
                {"error": "Data file or columns not found"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            df_people = pd.read_excel(request.FILES['data'], sheet_name='Personas')
            df_people = df_people.rename(columns={
                'Dirección': 'address',
                'Número de Casa': 'house_number',
                'Torre de Apartamento': 'apartment_tower',
                'Número de Apartamento': 'apartment_number',
                'Nombres': 'first_name',
                'Apellidos': 'last_name',
                'Cédula/Pasaporte': 'passport_id',
                'País': 'country',
                'Fecha de Nacimiento': 'birthday',
                'Teléfono': 'phone_number',
                'Correo Electrónico': 'email',
            })

            df_people['email'] = df_people['email'].fillna('')
            df_people['phone_number'] = df_people['phone_number'].fillna('')

        except KeyError:
            return Response(
                {"error": "Data file or columns not found"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            df_vehicles = pd.read_excel(request.FILES['data'], sheet_name='Vehículos')
            df_vehicles = df_vehicles.rename(columns={
                'Dirección': 'address',
                'Número de Casa': 'house_number',
                'Torre de Apartamento': 'apartment_tower',
                'Número de Apartamento': 'apartment_number',
                'Tipo': 'type',
                'Otro Tipo': 'type_other',
                'Marca': 'brand',
                'Modelo': 'model',
                'Color': 'color',
                'Placa': 'plate',
                'Nombre del Conductor': 'driver_name',
                'Cédula del Conductor': 'driver_id',
                'Teléfono del Conductor': 'phone',
            })

            df_vehicles['type_other'] = df_vehicles['type_other'].fillna('')

        except KeyError:
            return Response(
                {"error": "Data file or columns not found"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        for _, data in df_housings.iterrows():
            housing, created = Housing.objects.get_or_create(
                address=data['address'],
                building_type=data['building_type'],
                house_number=data['house_number'],
                apartment_tower=data['apartment_tower'],
                building_admin_name=data['building_admin_name'],
                apartment_number=data['apartment_number'],
                apartment_floor=data['apartment_floor'],
                is_owner=data['is_owner'],
                owner_name=data['owner_name'],
                owner_phone_number=data['owner_phone_number'],
                created_by=request.user,
            )

            if not created:
                continue

            for _, person in df_people.iterrows():
                if not is_same_housing(housing, person):
                    continue

                try:
                    country = Country.objects.get(name=person['country'])
                except Country.DoesNotExist:
                    country = Country.objects.get(name='Panamá')

                HousingPerson.objects.create(
                    first_name=person['first_name'],
                    last_name=person['last_name'],
                    passport_id=person['passport_id'],
                    country=country,
                    birthday=person['birthday'],
                    phone_number=person['phone_number'],
                    email=person['email'],
                    housing=housing,
                )

            for _, vehicle in df_vehicles.iterrows():
                if not is_same_housing(housing, vehicle):
                    continue

                housing.vehicles.create(
                    type=vehicle['type'],
                    type_other=vehicle['type_other'],
                    brand=vehicle['brand'],
                    model=vehicle['model'],
                    color=vehicle['color'],
                    plate=vehicle['plate'],
                    driver_name=vehicle['driver_name'],
                    driver_id=vehicle['driver_id'],
                    phone=vehicle['phone'],
                )

        return Response(
            {"message": "Data imported successfully"},
            status=status.HTTP_200_OK,
        )


class HousingPersonViewSet(ModelViewSet):
    queryset = HousingPerson.objects.all()
    serializer_class = HousingPersonSerializer
    filterset_fields = ['housing']
    pagination_class = None
