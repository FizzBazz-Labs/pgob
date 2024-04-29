from enum import Enum

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import Group

from rest_framework import decorators, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.viewsets import ModelViewSet

from core.models import SiteConfiguration, AccreditationStatus
from core.serializers import SiteConfigurationSerializer, AccreditationsSerializer

from general_vehicle_accreditation.models import GeneralVehicleAccreditation
from general_vehicle_accreditation.serializers import GeneralVehicleAccreditationSerializer

from intercom_equipment_declaration.models import IntercomEquipmentDeclaration
from intercom_equipment_declaration.serializers import IntercomEquipmentDeclarationSerializer

from international_accreditation.models import InternationalAccreditation

from national_accreditation.models import NationalAccreditation

from overflight_non_commercial_aircraft.models import OverflightNonCommercialAircraft
from overflight_non_commercial_aircraft.serializers import OverflightNonCommercialAircraftReadSerializer

from security_accreditations.models import SecurityWeaponAccreditation
from security_accreditations.serializers import SecurityWeaponAccreditationSerializer

from vehicle_access_airport_accreditations.models import VehicleAccessAirportAccreditations
from vehicle_access_airport_accreditations.serializers import VehicleAccessAirportAccreditationsSerializer

from pgob_auth.permissions import IsAdmin, IsReviewer


class SiteConfigurationView(RetrieveUpdateAPIView):
    serializer_class = SiteConfigurationSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]

        return [IsAdmin()]

    def get_object(self):
        return SiteConfiguration.objects.first()


class StandardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    # max_page_size = 1000


class AccreditationItem(Enum):
    NATIONAL = 'national'
    INTERNATIONAL = 'international'


class AccreditationListView(APIView):

    def paginate_querysets(self, querysets, request):
        paginated_response = {}
        paginator = StandardPagination()

        for key, queryset in querysets.items():

            try:
                page = paginator.paginate_queryset(queryset, request)

                if page is not None:
                    paginated_response[key] = paginator.get_paginated_response(
                        page).data

                else:
                    paginated_response[key] = queryset
            except:
                paginated_response[key] = paginator.get_paginated_response(
                    []).data

        return paginated_response

    def filter_queryset(self, querysets, request):

        filtered_querysets = {}
        country = request.query_params.get('country', None)
        status = request.query_params.get('status', None)
        accreditation_type = request.query_params.get('type', None)
        print(accreditation_type)

        for key, queryset in querysets.items():

            if accreditation_type is not None and accreditation_type != "''" and accreditation_type != '':

                if accreditation_type == AccreditationItem.NATIONAL.value:
                    queryset = [
                        item for item in queryset if item.get('type', None) == AccreditationItem.NATIONAL.value]
                elif accreditation_type == AccreditationItem.INTERNATIONAL.value:
                    print(accreditation_type)
                    queryset = [
                        item for item in queryset if item.get('type', None) == AccreditationItem.INTERNATIONAL.value]
                else:
                    if key == accreditation_type:
                        queryset = queryset
                    else:
                        queryset = []

            if status is not None and status != "''" and status != '':
                filter_dict = [
                    item for item in queryset if item['status'] == status]
                filtered_querysets[key] = filter_dict
            else:
                filtered_querysets[key] = queryset

        return filtered_querysets

    def has_admin_group(self):
        admin_groups = Group.objects.exclude(
            name='User').values_list('id', flat=True)

        return self.request.user.groups.filter(id__in=admin_groups).exists()

    def get_accreditations(self):
        data = []

        national_accreditations = NationalAccreditation.objects.filter(
            created_by=self.request.user)
        international_accreditations = InternationalAccreditation.objects.filter(
            created_by=self.request.user)

        if self.has_admin_group():
            national_accreditations = NationalAccreditation.objects.all()
            international_accreditations = InternationalAccreditation.objects.all()

        accreditation_list = list(
            national_accreditations) + list(international_accreditations)

        for item in accreditation_list:
            new_item = {
                'id': item.id,
                'first_name': item.first_name,
                'last_name': item.last_name,
                'status': item.status,
                'downloaded': item.downloaded,
                'created_at': item.created_at,
                'updated_at': item.updated_at,
                'created_by': {
                    'id': item.created_by.id,
                    'username': item.created_by.username,
                    'first_name': item.created_by.first_name,
                    'last_name': item.created_by.last_name,
                    'email': item.created_by.email,
                }
            }

            if isinstance(item, InternationalAccreditation):
                new_item['country'] = item.country.name
                new_item['type'] = AccreditationItem.INTERNATIONAL.value
            else:
                new_item['country'] = 'Panama'
                new_item['type'] = AccreditationItem.NATIONAL.value

            data.append(new_item)

        serializer = AccreditationsSerializer(data, many=True)
        return serializer.data

    def get_general_vehicles(self):
        vehicles = GeneralVehicleAccreditation.objects.filter(
            created_by=self.request.user)

        if self.has_admin_group():
            vehicles = GeneralVehicleAccreditation.objects.all()

        serializer = GeneralVehicleAccreditationSerializer(vehicles, many=True)
        return serializer.data

    def get_airport_access_vehicles(self):
        vehicles = VehicleAccessAirportAccreditations.objects.filter(
            created_by=self.request.user)

        if self.has_admin_group():
            vehicles = VehicleAccessAirportAccreditations.objects.all()

        serializer = VehicleAccessAirportAccreditationsSerializer(
            vehicles, many=True)

        return serializer.data

    def get_communication_equipments(self):
        equipments = IntercomEquipmentDeclaration.objects.filter(
            created_by=self.request.user)

        if self.has_admin_group():
            equipments = IntercomEquipmentDeclaration.objects.all()

        serializer = IntercomEquipmentDeclarationSerializer(
            equipments, many=True)

        return serializer.data

    def get_aircrafts(self):
        aircraft = OverflightNonCommercialAircraft.objects.filter(
            created_by=self.request.user)

        if self.has_admin_group():
            aircraft = OverflightNonCommercialAircraft.objects.all()

        serializer = OverflightNonCommercialAircraftReadSerializer(
            aircraft, many=True)

        return serializer.data

    def get_securities(self):
        securities = SecurityWeaponAccreditation.objects.filter(
            created_by=self.request.user)

        if self.has_admin_group():
            securities = SecurityWeaponAccreditation.objects.all()

        serializer = SecurityWeaponAccreditationSerializer(
            securities, many=True)

        return serializer.data

    def get(self, request):

        querysets = {
            'accreditations': self.get_accreditations(),
            'generalVehicles': self.get_general_vehicles(),
            'accessVehicles': self.get_airport_access_vehicles(),
            'equipments': self.get_communication_equipments(),
            'aircrafts': self.get_aircrafts(),
            'securities': self.get_securities(),
        }

        filtered_data = self.filter_queryset(querysets, request)
        pagination_querysets = self.paginate_querysets(filtered_data, request)

        return Response(pagination_querysets)


class ReviewAccreditationBase(APIView):
    model = None
    serializer_class = None
    permission_classes = [IsAuthenticated & IsReviewer]

    def patch(self, request: Request, pk, *args, **kwargs):
        try:
            item = self.model.objects.get(pk=pk)
            item.status = AccreditationStatus.REVIEWED
            item.reviewed_by = request.user
            item.reviewed_comment = request.data.get('reviewed_comment')
            item.save()

            serializer = self.serializer_class(item)
            return Response(serializer.data, status=HTTP_200_OK)

        except self.model.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)


class AccreditationViewSet(ModelViewSet):
    def get_permissions(self):
        match self.action:
            case 'retrieve':
                permissions = [AllowAny]

            case _:
                permissions = [IsAuthenticated]

        return [permission() for permission in permissions]

    @decorators.action(detail=True, methods=['patch'])
    def approve(self, request, pk: None, *args, **kwargs):
        try:
            item = self.get_queryset().get(pk=pk)
            item.status = AccreditationStatus.APPROVED
            item.authorized_by = request.user
            item.authorized_comment = request.data.get('authorized_comment')
            item.save()

            serializer = self.get_serializer_class(item)
            return Response(serializer.data, status=HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @decorators.action(detail=True, methods=['patch'])
    def review(self, request, pk=None, *args, **kwargs):
        try:
            item = self.get_queryset().get(pk=pk)
            item.status = AccreditationStatus.REVIEWED
            item.reviewed_by = request.user
            item.reviewed_comment = request.data.get('reviewed_comment')
            item.save()

            serializer = self.get_serializer_class(item)
            return Response(serializer.data, status=HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @decorators.action(detail=True, methods=['patch'])
    def reject(self, request, pk=None, *args, **kwargs):
        try:
            item = self.get_queryset().get(pk=pk)
            item.status = AccreditationStatus.REJECTED
            item.rejected_by = request.user
            item.save()

            serializer = self.get_serializer_class(item)
            return Response(serializer.data, status=HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
