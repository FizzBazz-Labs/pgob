from django.shortcuts import render


from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from overflight_non_commercial_aircraft.models import OverflightNonCommercialAircraft
from overflight_non_commercial_aircraft.serializers import OverflightNonCommercialAircraftSerializer, OverflightNonCommercialAircraftReadSerializer


class OverflightNonCommercialAircraftCreateApiView(ListCreateAPIView):
    queryset = OverflightNonCommercialAircraft.objects.all()
    serializer_class = OverflightNonCommercialAircraftSerializer
    permission_classes = [IsAuthenticated]


class OverflightNonCommercialAircraftRetrieveApiView(RetrieveAPIView):
    queryset = OverflightNonCommercialAircraft.objects.all()
    serializer_class = OverflightNonCommercialAircraftReadSerializer
    # permission_classes = [IsAuthenticated]
