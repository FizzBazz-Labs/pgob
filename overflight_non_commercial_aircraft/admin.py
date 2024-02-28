from django.contrib import admin

from overflight_non_commercial_aircraft.models import OverflightNonCommercialAircraft


@admin.register(OverflightNonCommercialAircraft)
class OverflightNonCommercialAircraftAdmin(admin.ModelAdmin):
    ...
