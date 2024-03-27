from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView

from vehicles.serializers import VehicleSerializer
from vehicles.models import Vehicle


class VehicleCreateView(CreateAPIView):
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        vehicle = Vehicle.objects.create(
            **request.data.dict())

        return Response({'vehicle_id': vehicle.id}, status=HTTP_201_CREATED)
