from django.contrib import admin

from international_accreditation.models import InternationalAccreditation


@admin.register(InternationalAccreditation)
class InternationalAccreditationAdmin(admin.ModelAdmin):
    ...
