from django.contrib import admin
from django.db import models
from django import forms
from django.utils.translation import gettext as _

from core.models import Country, Nationality, Position, MediaChannel,  CommunicationEquipmentDeclaration, EquipmentItem

from core.modelos.international_accreditation import InternationalAccreditation, MedicalHistory, Allergy, Inmunization

from core.modelos.national_accreditation import NationalAcreditation

from core.modelos.security_accreditation import SecurityAccreditation, CommunicationType, WeaponType

from core.modelos.flight_request import FlightRequest

from core.modelos.vehicle import Vehicle, VehicleAccreditation, VehicleTypes

from core.modelos.general_vehicle_accreditation import GeneralVehicleAccreditation 

#modelos = [Country, Nationality, Position, MediaChannel, NationalAcreditation, SecurityAccreditation, FlightRequest, Vehicle, VehicleAccreditation, CommunicationEquipmentDeclaration, EquipmentItem, GeneralVehicleAccreditation]

#for modelo in modelos:
#    admin.site.register(modelo)


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
    

@admin.register(Allergy)
class AllergyAdmin(admin.ModelAdmin): 
    ...


@admin.register(Inmunization)
class InmunizationAdmin(admin.ModelAdmin): 
    ...


@admin.register(MedicalHistory)
class MedicalHistoryAdmin(admin.ModelAdmin):
    ...


@admin.register(NationalAcreditation)
class NationalAcreditationAdmin(admin.ModelAdmin):
    
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
                'blood_type',
                'authorized_by',
                'date',
                'letter_of_authorization',
                'accreditation_type',
            ]
        })

    ]


@admin.register(SecurityAccreditation)
class  SecurityAccreditationAdmin(admin.ModelAdmin):

    fieldsets = [
        (_('control date'), {
            'fields': [
                'date_control',
                'time_control',
                'disclaimer_accepted',
            ]
        }),

        (_('weapon data'), {
            'fields': [
                'weapon',
                'brand',
                'model',
                'weapon_type',
                'serial_number',
                'caliber',
                'magazine_quantity',
                'ammunition_quantity',
            ]
        }),

        (_('communication equipment data'), {
            'fields': [
                'communication_radio',
                'communication_model',
                'communication_type',
                'communication_serial',
                'communication_frequency',
            ]
        })
    ]

    def render_change_form(self, request, context, *args, **kwargs):
        
        context['adminform'].form.fields['weapon_type'].widget = forms.CheckboxSelectMultiple(
            choices=[
                (item.id, item.name)
                for item in WeaponType.objects.all()
            ]
        )


        context['adminform'].form.fields['communication_type'].widget = forms.CheckboxSelectMultiple(
            choices=[
                (item.id, item.name)
                for item in CommunicationType.objects.all()
            ]
        )
        return super().render_change_form(request, context, *args, **kwargs)


@admin.register(WeaponType)
class WeaponTypeAdmin(admin.ModelAdmin):
    ...


@admin.register(CommunicationType)
class CommunicationTypeAdmin(admin.ModelAdmin):
    ...


@admin.register(FlightRequest)
class FlightRequestAdmin(admin.ModelAdmin):

    fieldsets = [
        (_('country'), {
            'fields': [
                'country'
            ]
        }),

        (_('aircraft data'), {
            'fields': [
                'aircraft_type',
                'model',
                'civilian_military',
                'registration_number',
                'color',
                'call_sign',
                'commander_name',
                'crew_members_count',
                'pmi_name',
                'position',
                'passengers_count',
            ]
        }),

        (_('flight information'), {
            'fields': [
                'entry_date',
                'exit_date',
                'overflight_info',
                'landing_info',
                'origin',
                'destination',
                'route',
                'ground_facilities',

            ]
        }),

        (_('signature and dates'), {
            'fields': [
                'request_date',
                'requester_signature',
            ]
        })
    ]


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):

    fieldsets = [
        (_('vehicle'), {
            'fields': [
                'vehicle_type',
                'brand',
                'color',
                'license_plate',
                'driver_name',
                'driver_id',
                'driver_phone',
            ]
        })
    ]


@admin.register(VehicleAccreditation)
class VehicleAccreditationAdmin(admin.ModelAdmin):
    
    fieldsets = [
        (_('country'),{
            'fields':[
                'country_name',
            ]
        }),

        (_('support vehicles'), {
            'fields':[
                'vehicles',
                'responsible_info',
                'responsible_signatures',
                'date',
            ]
        })
    ]


@admin.register(VehicleTypes)
class VehicleTypesAdmin(admin.ModelAdmin):
    ...


@admin.register(CommunicationEquipmentDeclaration)
class CommunicationEquipmentDeclarationAdmin(admin.ModelAdmin):
    ...


@admin.register(EquipmentItem)
class EquipmentItemAdmin(admin.ModelAdmin):
    ...


@admin.register(GeneralVehicleAccreditation)
class GeneralVehicleAccreditationAdmin(admin.ModelAdmin):
    
    fieldsets = [
        (_('general vehicle accreditation'), {
            'fields': [
                'mission',
                'vehicle_brand',
                'license_plate',
                'color',
                'driver_name',
                'dip',
                'assigned',
            ]
        }),

        (_('ministry of foreign affairs'), {
            'fields': [
                'distinctive',
                'observations',
                'responsible_signatures',
                'date',
            ]
        })
    ]