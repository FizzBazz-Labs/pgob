from django.contrib import admin
from django.utils.translation import gettext as _

from core.models import NationalAccreditation


@admin.register(NationalAccreditation)
class NationalAccreditationAdmin(admin.ModelAdmin):
    ...
