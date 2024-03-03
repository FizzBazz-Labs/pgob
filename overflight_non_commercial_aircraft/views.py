from django.shortcuts import render


from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from overflight_non_commercial_aircraft.models import OverflightNonCommercialAircraft
from overflight_non_commercial_aircraft.serializers import OverflightNonCommercialAircraftSerializer, OverflightNonCommercialAircraftReadSerializer


class OverflightNonCommercialAircraftCreateApiView(ListCreateAPIView):
    queryset = OverflightNonCommercialAircraft.objects.all()
    serializer_class = OverflightNonCommercialAircraftSerializer
    permission_classes = [IsAuthenticated]


class OverflightNonCommercialAircraftRetrieveApiView(RetrieveUpdateAPIView):
    queryset = OverflightNonCommercialAircraft.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return OverflightNonCommercialAircraftSerializer
        return OverflightNonCommercialAircraftReadSerializer
    permission_classes = [IsAuthenticated]
