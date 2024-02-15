from django.contrib import admin

from immunizations.models import Immunization


@admin.register(Immunization)
class ImmunizationAdmin(admin.ModelAdmin):
    ...