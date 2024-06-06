from django.conf import settings

from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from core.views import AccreditationViewSet
from credentials.utils import get_credential

from vehicle_access_airport_accreditations.models import VehicleAccessAirportAccreditations
from vehicle_access_airport_accreditations.serializers import (
    VehicleAccessAirportAccreditationsSerializer,
    VehicleAccessAirportAccreditationsReadSerializer)


class AirportVehicleAccessViewSet(AccreditationViewSet):
    queryset = VehicleAccessAirportAccreditations.objects.all()
    filterset_fields = ['status', 'country']
    search_fields = ['created_at__date']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return VehicleAccessAirportAccreditationsReadSerializer

        return VehicleAccessAirportAccreditationsSerializer

    @action(detail=True, methods=['patch'])
    def certificate(self, request: Request, pk=None, *args, **kwargs) -> Response:
        try:
            item = VehicleAccessAirportAccreditations.objects.get(pk=pk)
            template = settings.BASE_DIR / 'credentials' / \
                'templates' / 'credentials' / 'airport_vehicles_access.docx'

            folder_name = 'airport_vehicles_access'
            filename = 'Acceso_Vehiculos_Aeropuerto_' + item.country.name

            get_credential(item, template, filename, folder_name)

            return Response(
                {"message": "Accepted"},
                status=status.HTTP_202_ACCEPTED,
            )

        except VehicleAccessAirportAccreditations.DoesNotExist:
            return Response(
                {"error": "Certification config not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
