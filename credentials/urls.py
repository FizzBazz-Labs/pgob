from django.urls import path

from credentials.views import CertificateView

from credentials.utils import draw_overflight_permission

urlpatterns = [
    path('accreditations/certificate/<accreditation>/', CertificateView.as_view()),

    path('overflight-permission/<int:pk>/', draw_overflight_permission),
]
