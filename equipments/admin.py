from django.contrib import admin

from equipments.models import Equipment


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    ...
