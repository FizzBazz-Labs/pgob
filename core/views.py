from enum import Enum

from django.contrib.auth.models import Group
from rest_framework.response import Response
from rest_framework.views import APIView

from core.serializers import AccreditationsSerializer
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


class AccreditationItem(Enum):
    NATIONAL = 'national'
    INTERNATIONAL = 'international'


class AccreditationListView(APIView):
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

        accreditation_list = list(national_accreditations) + list(international_accreditations)

        for item in accreditation_list:
            new_item = {
                'id': item.id,
                'first_name': item.first_name,
                'last_name': item.last_name,
                'status': item.status,
                'download': item.downloaded,
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
        return Response({
            'accreditations': self.get_accreditations(),
            'generalVehicles': self.get_general_vehicles(),
            'accessVehicles': self.get_airport_access_vehicles(),
            'equipments': self.get_communication_equipments(),
            'aircrafts': self.get_aircrafts(),
            'securities': self.get_securities(),
        })
