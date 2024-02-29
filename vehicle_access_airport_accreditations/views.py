from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from vehicle_access_airport_accreditations.models import VehicleAccessAirportAccreditations

from vehicle_access_airport_accreditations.serializers import VehicleAccessAirportAccreditationsSerializer, VehicleAccessAirportAccreditationsReadSerializer

class VehicleAccessAirportAccreditationsListApiView(ListCreateAPIView):
    queryset = VehicleAccessAirportAccreditations.objects.all()
    serializer_class = VehicleAccessAirportAccreditationsSerializer

class VehicleAccessAirportAccreditationsRetrieveApiView(RetrieveAPIView):
    queryset = VehicleAccessAirportAccreditations.objects.all()
    serializer_class = VehicleAccessAirportAccreditationsReadSerializer