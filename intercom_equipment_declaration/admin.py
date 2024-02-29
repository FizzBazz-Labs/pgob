from django.contrib import admin

from .models import IntercomEquipmentDeclaration


@admin.register(IntercomEquipmentDeclaration)
class IntercomEquipmentDeclarationAdmin(admin.ModelAdmin):
    ...
