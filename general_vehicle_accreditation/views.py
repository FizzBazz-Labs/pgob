from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, UpdateAPIView

from general_vehicle_accreditation.models import GeneralVehicleAccreditation

from general_vehicle_accreditation.serializers import GeneralVehicleAccreditationSerializer, GeneralVehicleAccreditationReadSerializer

from rest_framework.permissions import IsAuthenticated

class GeneralVehicleAccreditationListApiView(ListCreateAPIView):
    queryset = GeneralVehicleAccreditation.objects.all()
    serializer_class = GeneralVehicleAccreditationSerializer
    permission_classes = [IsAuthenticated]

class GeneralVehicleAccreditationRetrieveApiView(UpdateAPIView):
    queryset = GeneralVehicleAccreditation.objects.all()
    serializer_class = GeneralVehicleAccreditationReadSerializer