from django.contrib import admin

from core.models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin): ...
