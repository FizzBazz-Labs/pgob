from django.contrib import admin

from .models import IntercomEquipmentDeclaration


@admin.register(IntercomEquipmentDeclaration)
class IntercomEquipmentDeclarationAdmin(admin.ModelAdmin):
    list_display = ('country', 'institution', 'status', 'created_at', 'updated_at')
    search_fields = ('institution',)
    list_filter = ('status', 'country')
