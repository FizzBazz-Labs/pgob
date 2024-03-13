from django.urls import path

from intercom_equipment_declaration.views import (
    IntercomEquipmentDeclarationListApiView,
    IntercomEquipmentDeclarationRetrieveApiView,
    ReviewAccreditation,
    ApproveAccreditation,
    RejectAccreditation
)

app_name = 'intercom_equipment_declaration'

urlpatterns = [
    path('intercom-equipment-declaration/',
         IntercomEquipmentDeclarationListApiView.as_view(), name='list-create'),
    path('intercom-equipment-declaration/<int:pk>/',
         IntercomEquipmentDeclarationRetrieveApiView.as_view(), name='detail'),

    path('<int:pk>/review/', ReviewAccreditation.as_view()),
    path('<int:pk>/approve/', ApproveAccreditation.as_view()),
    path('<int:pk>/reject/', RejectAccreditation.as_view()),
]
