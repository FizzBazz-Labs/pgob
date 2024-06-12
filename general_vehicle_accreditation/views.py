from io import BytesIO

import pandas as pd
from django.db.models import QuerySet
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from accreditations.mixins import ImportDataMixin, ExportDataMixin
from core.models import Certification, AccreditationStatus
from general_vehicle_accreditation.models import GeneralVehicleAccreditation as GeneralVehicle
from general_vehicle_accreditation.serializers import GeneralVehicleSerializer

from accreditations.views import AccreditationViewSet

from credentials.utils import certificate_vehicle_accreditation


class GeneralVehicleViewSet(ExportDataMixin, ImportDataMixin, AccreditationViewSet):
    queryset = GeneralVehicle.objects.all()
    serializer_class = GeneralVehicleSerializer
    filterset_fields = ['status', 'country', 'certificated']
    search_fields = ['created_at__date']

    @action(detail=True, methods=['patch'])
    def certificate(self, request: Request, pk=None, *args, **kwargs) -> Response:
        try:
            item = GeneralVehicle.objects.get(pk=pk)
            certificate_vehicle_accreditation(item)

            return Response(
                {"message": "Accepted"},
                status=status.HTTP_202_ACCEPTED,
            )

        except GeneralVehicle.DoesNotExist:
            return Response(
                {"error": "Certification config not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        except Certification.DoesNotExist:
            return Response(
                {"error": "Certification config not found."},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get_data_frame(self, queryset: QuerySet) -> pd.DataFrame:
        fields = [
            'id',
            'assigned_to',
            'country__name',
            'distinctive',
            'observations',
            'accreditation_type',
            'status',
        ]

        df = pd.DataFrame(queryset.values(*fields))

        df['accreditation_type'] = df['accreditation_type'].apply(
            lambda x: str(GeneralVehicle.AccreditationType(x).label),
        )
        df['status'] = df['status'].apply(
            lambda x: str(AccreditationStatus(x).label),
        )

        df = df.rename(columns={
            'id': 'ID',
            'assigned_to': 'Asignado A',
            'country__name': 'País',
            'distinctive': 'Distintivo',
            'observations': 'Observaciones',
            'accreditation_type': 'Tipo de Acreditación',
            'status': 'Estado',
        })

        return df
