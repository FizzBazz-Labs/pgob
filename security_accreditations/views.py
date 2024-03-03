from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from security_accreditations.models import SecurityWeaponAccreditation
from security_accreditations.serializers import SecurityWeaponAccreditationSerializer
from rest_framework.permissions import IsAuthenticated


class SecurityWeaponAccreditationCreateApiView(ListCreateAPIView):
    queryset = SecurityWeaponAccreditation.objects.all()
    serializer_class = SecurityWeaponAccreditationSerializer
    permission_classes = [IsAuthenticated]


class SecurityWeaponAccreditationRetrieveApiView(RetrieveUpdateAPIView):
    queryset = SecurityWeaponAccreditation.objects.all()
    serializer_class = SecurityWeaponAccreditationSerializer
    permission_classes = [IsAuthenticated]
