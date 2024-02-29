from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from intercom_equipment_declaration.models import IntercomEquipmentDeclaration

from intercom_equipment_declaration.serializers import IntercomEquipmentDeclarationSerializer, IntercomEquipmentDeclarationReadSerializer

class IntercomEquipmentDeclarationListApiView(ListCreateAPIView):
    queryset = IntercomEquipmentDeclaration.objects.all()
    serializer_class = IntercomEquipmentDeclarationSerializer

class IntercomEquipmentDeclarationRetrieveApiView(RetrieveAPIView):
    queryset = IntercomEquipmentDeclaration.objects.all()
    serializer_class = IntercomEquipmentDeclarationReadSerializer