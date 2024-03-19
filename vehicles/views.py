from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.permissions import IsAuthenticated

from vehicles.serializers import VehicleSerializer


class VehicleCreateView(APIView):
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # serializer = self.serializer_class(data=request.data)
        vehicles_data = request.FILES.getlist('vehicles[][driverLicense]')
        print(vehicles_data)
        print(request.POST.getlist('vehicles[][type]'))
        return Response(status=HTTP_201_CREATED)
