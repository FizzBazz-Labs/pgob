from django.contrib import admin

from core.models import Accreditation


@admin.register(Accreditation)
class AccreditationAdmin(admin.ModelAdmin):
    ...
