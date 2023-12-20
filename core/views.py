from django.shortcuts import render

from core.forms import NationalAccreditationForm


def get_national_accreditation_form(request):
    template = 'core/national_accreditation_form.html'

    context  = {
        'form': NationalAccreditationForm()
    }

    return render(request, template, context)
