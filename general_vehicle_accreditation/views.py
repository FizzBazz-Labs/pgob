from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter

from general_vehicle_accreditation.models import GeneralVehicleAccreditation as GeneralVehicle
from general_vehicle_accreditation.serializers import GeneralVehicleSerializer

from accreditations.views import AccreditationViewSet


class GeneralVehicleViewSet(AccreditationViewSet):
    queryset = GeneralVehicle.objects.all()
    serializer_class = GeneralVehicleSerializer
    filterset_fields = ['status', 'country']
    search_fields = ['created_at__date']
