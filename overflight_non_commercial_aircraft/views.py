from rest_framework.filters import SearchFilter

from django_filters.rest_framework import DjangoFilterBackend

from overflight_non_commercial_aircraft.models import OverflightNonCommercialAircraft
from overflight_non_commercial_aircraft.serializers import OverflightNonCommercialAircraftSerializer, \
    OverflightNonCommercialAircraftReadSerializer

from core.views import AccreditationViewSet


class OverflightNonCommercialAircraftViewSet(AccreditationViewSet):
    queryset = OverflightNonCommercialAircraft.objects.all()
    filterset_fields = ['status', 'country']
    search_fields = ['created_at__date']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return OverflightNonCommercialAircraftReadSerializer

        return OverflightNonCommercialAircraftSerializer
