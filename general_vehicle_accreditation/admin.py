from django.contrib import admin

from general_vehicle_accreditation.models import GeneralVehicleAccreditation as GeneralVehicle


@admin.register(GeneralVehicle)
class GeneralVehicleAdmin(admin.ModelAdmin):
    ...
