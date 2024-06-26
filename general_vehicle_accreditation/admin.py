from django.contrib import admin

from general_vehicle_accreditation.models import GeneralVehicleAccreditation as GeneralVehicle


@admin.register(GeneralVehicle)
class GeneralVehicleAdmin(admin.ModelAdmin):
    list_display = ('country', 'assigned_to', 'vehicle', 'observations', 'created_at', 'updated_at')
    search_fields = ('assigned_to','country')
    list_filter = ('assigned_to', 'country')
