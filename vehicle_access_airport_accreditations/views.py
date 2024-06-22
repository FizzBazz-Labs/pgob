import pandas as pd
from django.conf import settings
from django.db.models import QuerySet

from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from accreditations.mixins import ImportDataMixin, ExportDataMixin
from core.models import AccreditationStatus
from core.views import AccreditationViewSet
from credentials.utils import get_credential

from vehicle_access_airport_accreditations.models import VehicleAccessAirportAccreditations as VehicleAccess
from vehicle_access_airport_accreditations.serializers import (
    VehicleAccessAirportAccreditationsSerializer,
    VehicleAccessAirportAccreditationsReadSerializer,
)


class AirportVehicleAccessViewSet(ExportDataMixin, ImportDataMixin, AccreditationViewSet):
    queryset = VehicleAccess.objects.all()
    filterset_fields = ['status', 'country']
    search_fields = ['created_at__date']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return VehicleAccessAirportAccreditationsReadSerializer

        return VehicleAccessAirportAccreditationsSerializer

    @action(detail=True, methods=['patch'])
    def certificate(self, request: Request, pk=None, *args, **kwargs) -> Response:
        try:
            item = VehicleAccess.objects.get(pk=pk)
            template = settings.BASE_DIR / 'credentials' / \
                       'templates' / 'credentials' / 'airport_vehicles_access.docx'

            folder_name = 'airport_vehicles_access'
            filename = 'Acceso_Vehiculos_Aeropuerto_' + item.country.name

            get_credential(item, template, filename, folder_name)

            return Response(
                {"message": "Accepted"},
                status=status.HTTP_202_ACCEPTED,
            )

        except VehicleAccess.DoesNotExist:
            return Response(
                {"error": "Certification config not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

    def get_data_frame(self, queryset: QuerySet) -> pd.DataFrame:
        fields = {
            'id': 'ID',
            'information_responsible': 'Responsable de la Información',
            'country__name': 'País',
            'vehicles__driver_name': 'Nombre del Conductor',
            'vehicles__driver_id': 'Identificación del Conductor',
            'vehicles__plate': 'Placa',
            'vehicles__brand': 'Marca',
            'vehicles__model': 'Modelo',
            'status': 'Estado',
        }

        df = pd.DataFrame(queryset.values(*fields.keys()))
        df['status'] = df['status'].apply(
            lambda x: str(AccreditationStatus(x).label))

        return df.rename(columns=fields)
