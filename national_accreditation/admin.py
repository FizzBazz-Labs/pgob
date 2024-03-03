from django.contrib import admin

from national_accreditation.models import NationalAccreditation


@admin.register(NationalAccreditation)
class NationalAccreditationAdmin(admin.ModelAdmin):
    ...
