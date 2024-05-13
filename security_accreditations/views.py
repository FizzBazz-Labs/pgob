from rest_framework.filters import SearchFilter

from django_filters.rest_framework import DjangoFilterBackend

from security_accreditations.models import SecurityWeaponAccreditation
from security_accreditations.serializers import SecurityWeaponAccreditationSerializer

from core.views import AccreditationViewSet


class SecurityWeaponViewSet(AccreditationViewSet):
    queryset = SecurityWeaponAccreditation.objects.all()
    serializer_class = SecurityWeaponAccreditationSerializer
    filterset_fields = ['status', 'country']
