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
from core.utils import split_space
from core.views import AccreditationViewSet

from commerce.models import Commerce, CommerceEmployee
from commerce.serializers import CommerceSerializer, CommerceEmployeeSerializer
from countries.models import Country


class CommerceViewSet(AccreditationViewSet):
    queryset = Commerce.objects.all()
    serializer_class = CommerceSerializer
    filterset_fields = ['status']
    search_fields = ['created_at__date']

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.times_edited == 0:
            instance.times_edited += 1
            instance.save()

        return super().update(request, *args, **kwargs)

    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def export(self, request, *args, **kwargs) -> HttpResponse:
        queryset = Commerce.objects \
            .filter(status=Accreditation.Status.PENDING) \
            .prefetch_related('employees', 'employees__country')

        if not queryset.exists():
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)

        buffer = BytesIO()

        values = []

        for commerce in queryset:
            for person in commerce.employees.all():
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
            buffer,
            index=False,
            sheet_name='Personas',
        )

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
            df_commerces = pd.read_excel(request.FILES['data'], sheet_name='Comercios')
            df_commerces = df_commerces.rename(columns={
                'Nombre Comercial': 'commercial_name',
                'Razón Social': 'company_name',
                'Dirección': 'address',
                'Nombre del Administrador': 'admin_name',
                'Teléfono del Administrador': 'admin_phone_number',
                'Tipo de Comercio': 'commerce_type',
                'Otro Tipo de Comercio': 'commerce_type_other',
            })

        except KeyError:
            return Response(
                {"error": "Data file or columns not found"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            df_employees = pd.read_excel(request.FILES['data'], sheet_name='Empleados')
            df_employees = df_employees.rename(columns={
                'Comercio': 'commerce',
                'Nombres': 'first_name',
                'Apellidos': 'last_name',
                'Cédula/Pasaporte': 'passport_id',
                'País': 'country',
                'Fecha de Nacimiento': 'birthday',
                'Teléfono': 'phone_number',
                'Correo Electrónico': 'email',
                'Horario': 'schedule',
            })

        except KeyError:
            return Response(
                {"error": "Data file or columns not found"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            df_vehicles = pd.read_excel(request.FILES['data'], sheet_name='Vehículos')
            df_vehicles = df_vehicles.rename(columns={
                'Comercio': 'commerce',
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

        except KeyError:
            return Response(
                {"error": "Data file or columns not found"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        for _, data in df_commerces.iterrows():
            commerce, created = Commerce.objects.get_or_create(
                commercial_name=data['commercial_name'],
                company_name=data['company_name'],
                address=data['address'],
                admin_name=data['admin_name'],
                admin_phone_number=data['admin_phone_number'],
                commerce_type=data['commerce_type'],
                commerce_type_other=data['commerce_type_other'],
                created_by=request.user,
            )

            if not created:
                continue

            for _, employee in df_employees.iterrows():
                if employee['commerce'] != commerce.commercial_name:
                    continue

                try:
                    country = Country.objects.get(name=employee['country'])
                except Country.DoesNotExist:
                    country = Country.objects.get(name='Panamá')

                CommerceEmployee.objects.create(
                    commerce=commerce,
                    first_name=employee['first_name'],
                    last_name=employee['last_name'],
                    passport_id=employee['passport_id'],
                    country=country,
                    birthday=employee['birthday'],
                    phone_number=employee['phone_number'],
                    email=employee['email'],
                    schedule=employee['schedule'],
                )

            for _, vehicle in df_vehicles.iterrows():
                if vehicle['commerce'] != commerce.commercial_name:
                    continue

                commerce.vehicles.create(
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


class CommerceEmployeeViewSet(ModelViewSet):
    queryset = CommerceEmployee.objects.all()
    serializer_class = CommerceEmployeeSerializer
    filterset_fields = ['commerce']
    pagination_class = None
