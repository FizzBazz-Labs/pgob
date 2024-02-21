from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from core.forms import *
from core.models import *

from countries.models import Country

from positions.models import Position, SubPosition

from media_channels.models import MediaChannel

from immunizations.models import Immunization

from medical_histories.models import MedicalHistory


class NationalFormView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'core/national_form.html'
    model = NationalAccreditation
    form_class = NationalAccreditationForm
    success_url = reverse_lazy('core:national')
    success_message = "Formulario creado exitosamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['positions'] = Position.objects.all()
        context['types'] = NationalAccreditation.AccreditationType.choices
        context['sub_positions'] = SubPosition.objects.all()
        context['media_channels'] = MediaChannel.objects.all()

        return context


class OverflightAndNonCommercialAircraftFormView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'core/overflight_and_non_commercial_aircraft.html'
    model = OverflightNonCommercialAircraft
    form_class = OverflightNonCommercialAircraftForm
    success_url = reverse_lazy('core:overflight')
    success_message = 'Formulario creado exitosamente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['countries'] = Country.objects.all()
        context['jurisdictions'] = OverflightNonCommercialAircraft.Jurisdiction.choices
        context['positions'] = Position.objects.all()
        context['media_channels'] = MediaChannel.objects.all()

        return context


class InternationalFormView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'core/international_form.html'
    model = InternationalAccreditation
    form_class = InternationalAccreditationForm
    success_url = reverse_lazy('core:international')
    success_message = 'Formulario creado exitosamente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countries'] = Country.objects.all()

        context['inmunizations'] = Immunization.objects.all()
        context['positions'] = Position.objects.all()
        context['medicals'] = MedicalHistory.objects.all()
        context['types'] = InternationalAccreditation.AccreditationType.choices
        context['sub_positions'] = SubPosition.objects.all()
        context['media_channels'] = MediaChannel.objects.all()

        return context


class CreatedFormsView(LoginRequiredMixin, TemplateView):
    template_name = 'core/forms_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['national_forms'] = NationalAccreditation.objects.all()
        context['overflight'] = OverflightNonCommercialAircraft.objects.all()
        return context
