from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from security_accreditations.models import SecurityWeaponAccreditation
from security_accreditations.serializers import SecurityWeaponAccreditationSerializer


class SecurityWeaponAccreditationCreateApiView(ListCreateAPIView):
    queryset = SecurityWeaponAccreditation.objects.all()
    serializer_class = SecurityWeaponAccreditationSerializer
    # permission_classes = [IsAuthenticated]


class SecurityWeaponAccreditationRetrieveApiView(RetrieveAPIView):
    queryset = SecurityWeaponAccreditation.objects.all()
    serializer_class = SecurityWeaponAccreditationSerializer
    # permission_classes = [IsAuthenticated]
