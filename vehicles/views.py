from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from vehicles.models import Vehicle
from vehicles.serializers import VehicleSerializer


class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    # permission_classes = [IsAuthenticated]
