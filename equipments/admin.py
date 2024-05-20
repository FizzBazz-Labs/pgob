from django.contrib import admin

from equipments.models import Equipment


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
