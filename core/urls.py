from django.urls import path

from core.views import get_national_accreditation_form, get_international_accreditation_form

app_name = 'accreditation_forms'


urlpatterns = [
    path('', get_national_accreditation_form, name='national-accreditation'),
    path('international_accreditation/', get_international_accreditation_form, name='international-accreditation'),
]
