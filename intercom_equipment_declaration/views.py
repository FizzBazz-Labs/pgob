from intercom_equipment_declaration.models import IntercomEquipmentDeclaration
from intercom_equipment_declaration.serializers import IntercomEquipmentDeclarationSerializer

from core.views import AccreditationViewSet


class IntercomEquipmentDeclarationViewSet(AccreditationViewSet):
    queryset = IntercomEquipmentDeclaration.objects.all()
    serializer_class = IntercomEquipmentDeclarationSerializer
    filterset_fields = ['status', 'country']
