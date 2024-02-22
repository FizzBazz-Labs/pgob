from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DetailView

from core.forms import *
from core.models import *

from countries.models import Country
from immunizations.models import Immunization
from media_channels.models import MediaChannel
from medical_histories.models import MedicalHistory
from positions.models import Position, SubPosition


class AccreditationList(LoginRequiredMixin, TemplateView):
    template_name = 'core/accreditation_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['nationals'] = NationalAccreditation.objects.all()
        context['internationals'] = InternationalAccreditation.objects.all()

        return context


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
        context['blood_types'] = NationalAccreditation.BloodType.choices

        return context

    def get_success_url(self) -> str:
        return reverse_lazy(
            'core:national-detail',
            kwargs={'pk': self.object.pk}
        )


class NationalDetailView(LoginRequiredMixin, DetailView):
    template_name = 'core/na/detail.html'
    model = NationalAccreditation
    context_object_name = 'item'


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
        context['blood_types'] = NationalAccreditation.BloodType.choices

        if self.request.method == 'GET':
            context['sw_formset'] = SecurityWeaponFormSet
        else:
            context['sw_formset'] = SecurityWeaponFormSet(self.request.POST)

        return context

    # def form_valid(self, form):
    #     accreditation: InternationalAccreditation = form.save(commit=False)

    #     # Edecán Position ID
    #     if accreditation.position.pk != 10:
    #         return super().form_valid(form)

    #     sw_formset = SecurityWeaponFormSet(
    #         self.request.POST,
    #         instance=accreditation)

    #     for sw_form in sw_formset:
    #         if sw_form.instance.weapon == '':
    #             continue

    #         sw_form.instance.created_by = self.request.user.pk

    #     if not sw_formset.is_valid():
    #         return super().form_invalid(form)

    #     accreditation.save()
    #     sw_formset.save()

    #     return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy(
            'core:international-detail',
            kwargs={'pk': self.object.pk}
        )


class InternationalAccreditationDetail(LoginRequiredMixin, DetailView):
    template_name = 'core/ia/detail.html'
    model = InternationalAccreditation
    context_object_name = 'item'
