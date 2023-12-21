from django.shortcuts import render

from core.forms import NationalAccreditationForm, InternationalAccreditationForm, VehicleAccessToTheAirport


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

