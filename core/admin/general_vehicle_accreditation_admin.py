from django.contrib import admin
from django.utils.translation import gettext as _

from core.models import GeneralVehicleAccreditation


@admin.register(GeneralVehicleAccreditation)
class GeneralVehicleAccreditationAdmin(admin.ModelAdmin):
    ...
