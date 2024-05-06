from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK

from security_accreditations.models import SecurityWeaponAccreditation
from security_accreditations.serializers import SecurityWeaponAccreditationSerializer

from core.models import AccreditationStatus
from core.views import ReviewAccreditationBase, AccreditationViewSet

from pgob_auth.permissions import IsReviewer, IsAccreditor


class SecurityWeaponViewSet(AccreditationViewSet):
    queryset = SecurityWeaponAccreditation.objects.all()
    serializer_class = SecurityWeaponAccreditationSerializer
    filterset_fields = ['status', 'country']
