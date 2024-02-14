from django.contrib import admin
from django.db import models
from django import forms
from django.utils.translation import gettext as _

from core.models import *


@admin.register(OverflightNonCommercialAircraft)
class OverflightNonCommercialAircraftAdmin(admin.ModelAdmin):

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
