from core.views import AccreditationViewSet

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
