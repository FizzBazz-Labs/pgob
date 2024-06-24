from django.contrib import admin

from credentials.models import VehicleCertification


@admin.register(VehicleCertification)
class VehicleCertificationAdmin(admin.ModelAdmin):
    pass
