from general_vehicle_accreditation.models import GeneralVehicleAccreditation as GeneralVehicle
from general_vehicle_accreditation.serializers import GeneralVehicleSerializer

from accreditations.views import AccreditationViewSet


class GeneralVehicleViewSet(AccreditationViewSet):
    queryset = GeneralVehicle.objects.all()
    filterset_fields = ['status', 'country']
    serializer_class = GeneralVehicleSerializer
