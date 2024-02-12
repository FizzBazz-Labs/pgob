from django.shortcuts import render

#TEMPORAL
from django.http import HttpResponse

from core.forms import *


from core.modelos.national_accreditation import NationalAcreditation
from core.models import Position, Nationality, Country, MediaChannel




def get_national_accreditation_form(request):
    template = 'core/national_accreditation_form.html'

    if(request.method == "GET"):

        context  = {
            'form': NationalAccreditationForm()
        }

        return render(request, template, context)

    if(request.method == "POST"):
        return HttpResponse(request)






def get_international_accreditation_form(request):
    template = 'core/international_accreditation_form.html'

    context  = {
        'form': InternationalAccreditationForm()
    }

    return render(request, template, context)


def get_vehicle_access_to_the_airport_form(request):
    template = 'core/vehicle_access_to_the_airport_form.html'

    context = {
        'form': VehicleAccessAirportForm()
    }

    return render(request, template, context)


def get_overflight_and_non_commercial_aircraft_form(request):
    template = 'core/overflight_and_non_commercial_aircraft.html'

    context  = {
        'form': OverflightNonCommercialAircraftForm()
    }

    return render(request, template, context)


def get_medical_report_form(request):
    template = 'core/medical_report_form.html'

    context  = {
        'form': MedicalReportForm()
    }

    return render(request, template, context)


def get_security_weapons_registration_form(request):
    template = 'core/security_weapons_registration.html'

    context  = {
        'form': SecurityWeaponsRegistrationForm()
    }

    return render(request, template, context)


def get_newsletter_international_form(request):
    template = 'core/newsletter_international_accreditation_form.html'

    context  = {
        'form': NewsletterInternationalForm()
    }

    return render(request, template, context)


def get_newsletter_national_form(request):
    template = 'core/newsletter_national_accreditation_form.html'

    context  = {
        'form': NewsletterNationalForm()
    }

    return render(request, template, context)

