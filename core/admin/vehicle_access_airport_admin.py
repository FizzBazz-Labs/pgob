from django.contrib import admin
from django.db import models
from django import forms
from django.utils.translation import gettext as _

from core.models import *



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


@admin.register(VehicleAccessAirport)
class VehicleAccessAirport(admin.ModelAdmin):
    
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