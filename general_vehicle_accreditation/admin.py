from django.contrib import admin

from .models import GeneralVehicleAccreditation


@admin.register(GeneralVehicleAccreditation)
class GeneralVehicleAccreditationAdmin(admin.ModelAdmin):
    ...
