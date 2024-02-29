from django.contrib import admin

from .models import VehicleAccessAirportAccreditations


@admin.register(VehicleAccessAirportAccreditations)
class VehicleAccessAirportAccreditationsAdmin(admin.ModelAdmin):
    ...
