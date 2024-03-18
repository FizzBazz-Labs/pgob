from django.urls import path

from security_accreditations.views import (
    SecurityWeaponAccreditationCreateApiView,
    SecurityWeaponAccreditationRetrieveApiView,
    ReviewAccreditation,
    ApproveAccreditation,
    RejectAccreditation
)

urlpatterns = [
    path('', SecurityWeaponAccreditationCreateApiView.as_view(),
         name='create-list-security-accreditations'),
    path('<int:pk>/', SecurityWeaponAccreditationRetrieveApiView.as_view(),
         name='retrieve-security-accreditation'),

    path('<int:pk>/review/', ReviewAccreditation.as_view()),
    path('<int:pk>/approve/', ApproveAccreditation.as_view()),
    path('<int:pk>/reject/', RejectAccreditation.as_view()),

]
