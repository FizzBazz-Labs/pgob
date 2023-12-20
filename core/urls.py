from django.urls import path

from core.views import get_national_accreditation_form


urlpatterns = [
    path('', get_national_accreditation_form, name='national-accreditation'),
]
