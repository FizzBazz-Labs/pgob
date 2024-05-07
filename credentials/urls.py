from django.urls import path

from credentials.views import TestTemplate, TestWeaponAccreditation, CertificateView

urlpatterns = [
    path('test-template/', TestTemplate.as_view(), name='test-template'),
    path('test-weapon-accreditation/', TestWeaponAccreditation.as_view(),
         name='test-weapon-accreditation'),

    path('accreditations/certificate/<accreditation>/',
         CertificateView.as_view())
]
