from django.contrib import admin

from core.models import SiteConfiguration, Accreditation


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    ...


@admin.register(Accreditation)
class AccreditationAdmin(admin.ModelAdmin):
    ...
