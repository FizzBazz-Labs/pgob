from django.urls import path

from credentials.views import CertificateView

urlpatterns = [
    path('accreditations/certificate/<accreditation>/', CertificateView.as_view())
]
