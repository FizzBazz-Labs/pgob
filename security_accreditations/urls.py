from django.urls import path

from security_accreditations.views import SecurityWeaponAccreditationCreateApiView, SecurityWeaponAccreditationRetrieveApiView

urlpatterns = [
    path('security-accreditation/', SecurityWeaponAccreditationCreateApiView.as_view(),
         name='create-list-security-accreditations'),
    path('security-accreditation/<int:pk>/', SecurityWeaponAccreditationRetrieveApiView.as_view(),
         name='retrieve-security-accreditation')

]
