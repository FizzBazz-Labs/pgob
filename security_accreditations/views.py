from django.conf import settings


from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from security_accreditations.models import SecurityWeaponAccreditation
from security_accreditations.serializers import SecurityWeaponAccreditationSerializer

from core.views import AccreditationViewSet
from credentials.utils import get_credential


class SecurityWeaponViewSet(AccreditationViewSet):
    queryset = SecurityWeaponAccreditation.objects.all()
    serializer_class = SecurityWeaponAccreditationSerializer
    filterset_fields = ['status', 'country']

    @action(detail=True, methods=['patch'])
    def certificate(self, request: Request, pk=None, *args, **kwargs) -> Response:
        try:
            item = SecurityWeaponAccreditation.objects.get(pk=pk)
            template = settings.BASE_DIR / 'credentials' / \
                'templates' / 'credentials' / 'security_weapons.docx'

            filename = f'Acreditacion_armas_{
                item.country.name}_{item.passport_id}'
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
