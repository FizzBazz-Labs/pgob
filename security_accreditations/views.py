import pandas as pd
from django.conf import settings
from django.db.models import QuerySet

from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from accreditations.mixins import ExportDataMixin, ImportDataMixin
from core.models import AccreditationStatus
from security_accreditations.models import SecurityWeaponAccreditation
from security_accreditations.serializers import SecurityWeaponAccreditationSerializer

from core.views import AccreditationViewSet
from credentials.utils import get_credential


class SecurityWeaponViewSet(ExportDataMixin, ImportDataMixin, AccreditationViewSet):
    queryset = SecurityWeaponAccreditation.objects.all()
    serializer_class = SecurityWeaponAccreditationSerializer
    filterset_fields = ['status', 'country']

    @action(detail=True, methods=['patch'])
    def certificate(self, request: Request, pk=None, *args, **kwargs) -> Response:
        try:
            item = SecurityWeaponAccreditation.objects.get(pk=pk)
            template = settings.BASE_DIR / 'credentials' / 'templates' / 'credentials' / 'security_weapons.docx'

            filename = f'Acreditacion_armas_{item.country.name}_{item.passport_id}'
            folder_name = 'security_weapon_accreditation'

            get_credential(item, template, filename, folder_name)

            return Response(
                {"message": "Accepted"},
                status=status.HTTP_202_ACCEPTED,
            )

        except SecurityWeaponAccreditation.DoesNotExist:
            return Response(
                {"error": "Certification config not found."},
                status=status.HTTP_404_NOT_FOUND
            )

    def get_data_frame(self, queryset: QuerySet) -> pd.DataFrame:
        fields = [
            'id',
            'country__name',
            'name',
            'passport_id',
            'position__name',
            'control_datetime',
            'observations',
            'permit_number',
            'flight_arrival_datetime',
            'flight_departure_datetime',
            'status',
        ]

        df = pd.DataFrame(queryset.values(*fields))

        df['status'] = df['status'].apply(
            lambda x: str(AccreditationStatus(x).label),
        )

        df['control_datetime'] = df['control_datetime'].apply(
            lambda x: x.strftime('%d-%m-%Y %H:%M') if not pd.isnull(x) else 'N/A',
        )

        df['flight_arrival_datetime'] = df['flight_arrival_datetime'].apply(
            lambda x: x.strftime('%d-%m-%Y %H:%M') if not pd.isnull(x) else 'N/A',
        )

        df['flight_departure_datetime'] = df['flight_departure_datetime'].apply(
            lambda x: x.strftime('%d-%m-%Y %H:%M') if not pd.isnull(x) else 'N/A',
        )

        df = df.rename(columns={
            'id': 'ID',
            'country__name': 'País',
            'name': 'Nombre',
            'passport_id': 'Pasaporte',
            'position__name': 'Cargo',
            'control_datetime': 'Fecha y hora de Control',
            'observations': 'Observaciones',
            'permit_number': 'Número de Permiso',
            'flight_arrival_datetime': 'Fecha y hora de llegada',
            'flight_departure_datetime': 'Fecha y hora de salida',
            'status': 'Estado',
        })

        return df
