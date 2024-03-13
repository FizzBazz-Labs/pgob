from django.urls import path

from security_accreditations.views import (
    SecurityWeaponAccreditationCreateApiView,
    SecurityWeaponAccreditationRetrieveApiView,
    ReviewAccreditation,
    ApproveAccreditation,
    RejectAccreditation
)

urlpatterns = [
    path('security-weapon-accreditation/', SecurityWeaponAccreditationCreateApiView.as_view(),
         name='create-list-security-accreditations'),
    path('security-weapon-accreditation/<int:pk>/', SecurityWeaponAccreditationRetrieveApiView.as_view(),
         name='retrieve-security-accreditation'),

    path('<int:pk>/review/', ReviewAccreditation.as_view()),
    path('<int:pk>/approve/', ApproveAccreditation.as_view()),
    path('<int:pk>/reject/', RejectAccreditation.as_view()),

]
