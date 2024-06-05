from django.urls import path

from credentials.views import CertificateView, generate_pdf, generate_communication_equipment_pdf, generate_weapons_pdf

from credentials.utils import draw_overflight_permission

urlpatterns = [
    path('accreditations/certificate/<accreditation>/', CertificateView.as_view()),

    path('overflight-permission/<int:pk>/', draw_overflight_permission),

    path('airport-vehicles/', generate_pdf),
    path('equipment-declaration/', generate_communication_equipment_pdf),
    path('security-weapon/', generate_weapons_pdf),
]
