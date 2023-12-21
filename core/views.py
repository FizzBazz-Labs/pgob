from django.shortcuts import render

from core.forms import *


def get_national_accreditation_form(request):
    template = 'core/national_accreditation_form.html'

    context  = {
        'form': NationalAccreditationForm()
    }

    return render(request, template, context)


def get_international_accreditation_form(request):
    template = 'core/international_accreditation_form.html'

    context  = {
        'form': InternationalAccreditationForm()
    }

    return render(request, template, context)


def get_vehicle_access_to_the_airport_form(request):
    template = 'core/vehicle_access_to_the_airport_form.html'

    context = {
        'form': VehicleAccessToTheAirport
    }

    return render(request, template, context)


def get_overflight_and_non_commercial_aircraft_form(request):
    template = 'core/overflight_and_non_commercial_aircraft.html'

    context  = {
        'form': OverflightAndNonCommercialAircraft()
    }

    return render(request, template, context)
