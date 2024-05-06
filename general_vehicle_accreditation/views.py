from general_vehicle_accreditation.models import GeneralVehicleAccreditation as GeneralVehicle
from general_vehicle_accreditation.serializers import GeneralVehicleAccreditationSerializer, \
    GeneralVehicleAccreditationReadSerializer

from core.views import AccreditationViewSet

from countries.models import Country


class GeneralVehicleViewSet(AccreditationViewSet):
    queryset = GeneralVehicle.objects.all()
    filterset_fields = ['status', 'country']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return GeneralVehicleAccreditationReadSerializer

        return GeneralVehicleAccreditationSerializer
