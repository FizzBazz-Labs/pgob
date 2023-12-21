from django.urls import path

from core.views import *


app_name = 'accreditation'

urlpatterns = [
    path(
        'national_accreditation/',
        get_national_accreditation_form,
        name='national-accreditation',
    ),

    path(
        'international_accreditation/',
        get_international_accreditation_form,
        name='international-accreditation',
    ),

    path(
        'overflight_and_non_commercial_aircraft_accreditation/',
        get_overflight_and_non_commercial_aircraft_form,
        name='overflight-and-non-commercial-aircraft-accreditation',
    ),
    
    path(
        'vehicle_access_to_the_airport/',
        get_vehicle_access_to_the_airport_form,
        name='vehicle-access-to-the-airport',
    ),
]
