from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from vehicle_access_airport_accreditations.models import VehicleAccessAirportAccreditations

from vehicle_access_airport_accreditations.serializers import VehicleAccessAirportAccreditationsSerializer, VehicleAccessAirportAccreditationsReadSerializer

from rest_framework.permissions import IsAuthenticated

class VehicleAccessAirportAccreditationsListApiView(ListCreateAPIView):
    queryset = VehicleAccessAirportAccreditations.objects.all()
    serializer_class = VehicleAccessAirportAccreditationsSerializer
    permission_classes = [IsAuthenticated]

class VehicleAccessAirportAccreditationsRetrieveApiView(RetrieveAPIView):
    queryset = VehicleAccessAirportAccreditations.objects.all()
    serializer_class = VehicleAccessAirportAccreditationsReadSerializer
