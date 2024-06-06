from django.conf import settings

from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from intercom_equipment_declaration.models import IntercomEquipmentDeclaration
from intercom_equipment_declaration.serializers import IntercomEquipmentDeclarationSerializer

from core.views import AccreditationViewSet
from credentials.utils import get_credential


class IntercomEquipmentDeclarationViewSet(AccreditationViewSet):
    queryset = IntercomEquipmentDeclaration.objects.all()
    serializer_class = IntercomEquipmentDeclarationSerializer
    filterset_fields = ['status', 'country']
    search_fields = ['created_at__date']

    @action(detail=True, methods=['patch'])
    def certificate(self, request: Request, pk=None, *args, **kwargs) -> Response:
        try:
            item = IntercomEquipmentDeclaration.objects.get(pk=pk)
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

        except IntercomEquipmentDeclaration.DoesNotExist:
            return Response(
                {"error": "Certification config not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
