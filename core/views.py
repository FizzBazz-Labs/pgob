# from rest_framework.generics import
from typing import Any
from rest_framework.views import APIView
from rest_framework.response import Response

from core.serializers import AccreditationsSerializer, UserSerializer

from international_accreditation.models import InternationalAccreditation
from national_accreditation.models import NationalAccreditation

from general_vehicle_accreditation.models import GeneralVehicleAccreditation
from general_vehicle_accreditation.serializers import GeneralVehicleAccreditationSerializer

from vehicle_access_airport_accreditations.models import VehicleAccessAirportAccreditations
from vehicle_access_airport_accreditations.serializers import VehicleAccessAirportAccreditationsSerializer

from intercom_equipment_declaration.models import IntercomEquipmentDeclaration
from intercom_equipment_declaration.serializers import IntercomEquipmentDeclarationSerializer

from overflight_non_commercial_aircraft.models import OverflightNonCommercialAircraft
from overflight_non_commercial_aircraft.serializers import OverflightNonCommercialAircraftSerializer

from security_accreditations.models import SecurityWeaponAccreditation
from security_accreditations.serializers import SecurityWeaponAccreditationSerializer


class AccreditationListView(APIView):

    def has_admin_group(self):
        return self.request.user.groups.filter(name='admin').exists()

    def get_accreditations(self):
        data = []
        national_accreditations = NationalAccreditation.objects.filter(
            created_by=self.request.user)
        international_accreditations = InternationalAccreditation.objects.filter(
            created_by=self.request.user)

        if self.has_admin_group():
            national_accreditations = NationalAccreditation.objects.all()
            international_accreditations = InternationalAccreditation.objects.all()

        accreditation_list = list(national_accreditations) + \
            list(international_accreditations)

        for item in accreditation_list:
            new_item = {
                'id': item.id,
                'first_name': item.first_name,
                'last_name': item.last_name,

                'status': item.status,
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
                new_item['type'] = 'International'
            else:
                new_item['country'] = 'Panama'
                new_item['type'] = 'National'

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

        serializer = OverflightNonCommercialAircraftSerializer(
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
