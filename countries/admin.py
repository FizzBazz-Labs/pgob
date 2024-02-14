from django.contrib import admin

from countries.models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['name', 'nationality']
