from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from core.forms import *
from core.models import NationalAccreditation

from countries.models import Country

from positions.models import Position, SubPosition

from media_channels.models import MediaChannel


class NationalFormView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'core/national_form.html'
    model = NationalAccreditation
    form_class = NationalAccreditationForm
    success_url = reverse_lazy('core:national')
    success_message = "Formulario creado exitosamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context['countries'] = Country.objects.all()
        context['positions'] = Position.objects.all()
        context['types'] = NationalAccreditation.AccreditationType.choices
        context['media_channels'] = MediaChannel.objects.all()

        return context

# def get_national_accreditation_form(request):
    # template = 'core/national_accreditation_form.html'

    # if(request.method == "GET"):

    #     context  = {
    #         'form': NationalAccreditationForm()
    #     }

    #     return render(request, template, context)

    # if(request.method == "POST"):
    #     return HttpResponse(request)


# prueba
# def get_national_accreditation_form(request):
#     national_accreditation =  NationalAccreditationForm
#     return render_to_response ()


# def get_international_accreditation_form(request):
#     template = 'core/international_accreditation_form.html'

#     context  = {
#         'form': InternationalAccreditationForm()
#     }

#     return render(request, template, context)


# def get_vehicle_access_to_the_airport_form(request):
#     template = 'core/vehicle_access_to_the_airport_form.html'

#     context = {
#         'form': VehicleAccessAirportForm()
#     }

#     return render(request, template, context)


# def get_overflight_and_non_commercial_aircraft_form(request):
#     template = 'core/overflight_and_non_commercial_aircraft.html'

#     context  = {
#         'form': OverflightNonCommercialAircraftForm()
#     }

#     return render(request, template, context)


# def get_medical_report_form(request):
#     template = 'core/medical_report_form.html'

#     context  = {
#         'form': MedicalReportForm()
#     }

#     return render(request, template, context)


# def get_security_weapons_registration_form(request):
#     template = 'core/security_weapons_registration.html'

#     context  = {
#         'form': SecurityWeaponsRegistrationForm()
#     }

#     return render(request, template, context)


# def get_newsletter_international_form(request):
#     template = 'core/newsletter_international_accreditation_form.html'

#     context  = {
#         'form': NewsletterInternationalForm()
#     }

#     return render(request, template, context)


# def get_newsletter_national_form(request):
#     template = 'core/newsletter_national_accreditation_form.html'

#     context  = {
#         'form': NewsletterNationalForm()
#     }

#     return render(request, template, context)
