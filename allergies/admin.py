from django.contrib import admin

from allergies.models import Allergy


@admin.register(Allergy)
class AllergyAdmin(admin.ModelAdmin):
    ...