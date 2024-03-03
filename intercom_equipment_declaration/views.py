from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from intercom_equipment_declaration.models import IntercomEquipmentDeclaration

from intercom_equipment_declaration.serializers import IntercomEquipmentDeclarationSerializer, IntercomEquipmentDeclarationReadSerializer

from rest_framework.permissions import IsAuthenticated

class IntercomEquipmentDeclarationListApiView(ListCreateAPIView):
    queryset = IntercomEquipmentDeclaration.objects.all()
    serializer_class = IntercomEquipmentDeclarationSerializer
    permission_classes = [IsAuthenticated]

class IntercomEquipmentDeclarationRetrieveApiView(RetrieveUpdateAPIView):
    queryset = IntercomEquipmentDeclaration.objects.all()
    serializer_class = IntercomEquipmentDeclarationReadSerializer