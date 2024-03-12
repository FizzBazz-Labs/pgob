from django.contrib import admin

from national_accreditation.models import NationalAccreditation


@admin.register(NationalAccreditation)
class NationalAccreditationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'passport_id', 'position', 'id')
