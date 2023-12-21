from django.urls import path

from core.views import get_national_accreditation_form, get_international_accreditation_form, get_vehicle_access_to_the_airport_form

app_name = 'accreditation_forms'


urlpatterns = [
    path('', get_national_accreditation_form, name='national-accreditation'),
    path('international_accreditation/', get_international_accreditation_form, name='international-accreditation'),
    path('vehicle_access_to_the_airport/', get_vehicle_access_to_the_airport_form, name='vehicle-access-to-the-airport')
]
