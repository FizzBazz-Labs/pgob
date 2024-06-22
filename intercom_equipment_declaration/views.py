import pandas as pd
from django.conf import settings
from django.db.models import QuerySet

from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from accreditations.mixins import ExportDataMixin, ImportDataMixin
from core.models import AccreditationStatus
from intercom_equipment_declaration.models import IntercomEquipmentDeclaration as Communication
from intercom_equipment_declaration.serializers import IntercomEquipmentDeclarationSerializer

from core.views import AccreditationViewSet
from credentials.utils import get_credential


class IntercomEquipmentDeclarationViewSet(ExportDataMixin, ImportDataMixin, AccreditationViewSet):
    queryset = Communication.objects.all()
    serializer_class = IntercomEquipmentDeclarationSerializer
    filterset_fields = ['status', 'country']
    search_fields = ['created_at__date']

    @action(detail=True, methods=['patch'])
    def certificate(self, request: Request, pk=None, *args, **kwargs) -> Response:
        try:
            item = Communication.objects.get(pk=pk)
            template = settings.BASE_DIR / 'credentials' / \
                       'templates' / 'credentials' / 'intercom_equipments.docx'

            filename = f'Equipos_Intercomunicacion_{
            item.country.name}_{item.institution}'
            folder_name = 'intercom_equipment_declaration'

            get_credential(item, template, filename, folder_name)

            return Response(
                {"message": "Accepted"},
                status=status.HTTP_202_ACCEPTED,
            )

        except Communication.DoesNotExist:
            return Response(
                {"error": "Certification config not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

    def get_data_frame(self, queryset: QuerySet) -> pd.DataFrame:
        fields = {
            'id': 'ID',
            'institution': 'Institución',
            'country__name': 'País',
            'equipments__brand': 'Marca',
            'equipments__model': 'Modelo',
            'equipments__type': 'Tipo',
            'equipments__serial': 'Serial No.',
            'equipments__frequency': 'Frecuencia',
            'equipments__value': 'Valor',
            'status': 'Estado',
        }

        df = pd.DataFrame(queryset.values(*fields.keys()))
        df['status'] = df['status'].apply(
            lambda x: str(AccreditationStatus(x).label),
        )

        return df.rename(columns=fields)
