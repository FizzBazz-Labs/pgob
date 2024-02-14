from django.urls import path

from core.views import *


app_name = 'core'

urlpatterns = [
    path('', NationalFormView.as_view(), name='national')
    # path(
    #     '',
    #     get_national_accreditation_form,
    #     name='national-accreditation',
    # ),

    # path(
    #     'international_accreditation/',
    #     get_international_accreditation_form,
    #     name='international-accreditation',
    # ),

    # path(
    #     'overflight_and_non_commercial_aircraft_accreditation/',
    #     get_overflight_and_non_commercial_aircraft_form,
    #     name='overflight-and-non-commercial-aircraft-accreditation',
    # ),

    # path(
    #     'vehicle_access_to_the_airport/',
    #     get_vehicle_access_to_the_airport_form,
    #     name='vehicle-access-to-the-airport',
    # ),

    # path(
    #     'medical_report/',
    #     get_medical_report_form,
    #     name='medical-report',
    # ),

    # path(
    #     'security_weapons_registration/',
    #     get_security_weapons_registration_form,
    #     name='security-weapons-registration',
    # ),

    # path(
    #     'newsletter_international/',
    #     get_newsletter_international_form,
    #     name='newsletter-international',
    # ),

    # path(
    #     'newsletter_national/',
    #     get_newsletter_national_form,
    #     name='newsletter-national',
    # ),

]
