from django.shortcuts import render

from core.forms import NationalAccreditationForm, InternationalAccreditationForm


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

