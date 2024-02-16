from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from core.models import VehicleAccessAirport, Vehicle


class VehicleInline(admin.TabularInline):
    model = Vehicle


@admin.register(VehicleAccessAirport)
class VehicleAccessAirport(admin.ModelAdmin):
    inlines = [VehicleInline]
