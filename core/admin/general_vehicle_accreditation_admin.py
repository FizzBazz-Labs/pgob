from django.contrib import admin
from django.db import models
from django import forms
from django.utils.translation import gettext as _

from core.models import *


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