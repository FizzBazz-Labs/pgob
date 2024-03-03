from django.urls import path

from intercom_equipment_declaration.views import IntercomEquipmentDeclarationListApiView, IntercomEquipmentDeclarationRetrieveApiView

app_name = 'intercom_equipment_declaration'

urlpatterns = [
    path('intercom_equipment_declaration/',
         IntercomEquipmentDeclarationListApiView.as_view(), name='list-create'),
    path('intercom_equipment_declaration/<int:pk>/',
         IntercomEquipmentDeclarationRetrieveApiView.as_view(), name='detail'),
]
