from django.contrib import admin
from django.db import models
from django import forms
from django.utils.translation import gettext as _

from core.models import *

@admin.register(InternationalAccreditation)
class InternationalAccreditationAdmin(admin.ModelAdmin):
    
    fieldsets = [
        (_('Personal Info'), {
            'fields': [
                'first_name',
                'last_name',
                'image',
                'nationality',
                'passport_id',
                'position',
                'media_channel',
                'institution',
                'address',
                'phone',
                'cellphone',
                'email',
                'birthday',
                'birthplace',
                'authorized_by',
                'date',
                'letter_of_authorization',
                'accreditation_type',
            ]
        }),
        
        (_('Medical Data'), {
            'fields': [
                'blood_type',
                'age',
                'diseases_under_treatment',
                'medications_in_use',
                'have_allergies',
                'allergies',
                'has_inmunizations',
                'inmunizations',
                'have_medical_history',
                'medical_histories',
                'surgical_history',
                'has_personal_doctor',
                'doctor_name',
            ]
        }),
        
        (_('Accomodation Info'), {
            'fields': [
                'hotel_name',
                'hotel_address',
                'hotel_phone',
            ]
        }),
        
        (_('Flights Information'), {
            'fields': [
                'flight_arrival_date',
                'flight_arrival_time',
                'flight_arrival_number',
                'fligth_procedence',
                'flight_departure_date',
                'flight_departure_time',
                'flight_departure_number',
                'flight_destination',
            ]
        })
    ]
    
    def render_change_form(self, request, context, *args, **kwargs):
        
        context['adminform'].form.fields['medical_histories'].widget = forms.CheckboxSelectMultiple(
            choices=[
                (item.id, item.name)
                for item in MedicalHistory.objects.all()
            ]
        )
        
        context['adminform'].form.fields['allergies'].widget = forms.CheckboxSelectMultiple(
            choices=[
                (item.id, item.name)
                for item in Allergy.objects.all()
            ]
        )
        
        context['adminform'].form.fields['inmunizations'].widget = forms.CheckboxSelectMultiple(
            choices=[
                (item.id, item.name)
                for item in Inmunization.objects.all()
            ]
        )
        return super().render_change_form(request, context, *args, **kwargs)
    

# @admin.register(Allergy)
# class AllergyAdmin(admin.ModelAdmin): 
#     ...


# @admin.register(Inmunization)
# class InmunizationAdmin(admin.ModelAdmin): 
#     ...


# @admin.register(MedicalHistory)
# class MedicalHistoryAdmin(admin.ModelAdmin):
#     ...