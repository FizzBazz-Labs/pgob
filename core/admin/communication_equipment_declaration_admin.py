from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from core.models import CommunicationEquipmentDeclaration, EquipmentItem


class EquipmentItemInline(admin.TabularInline):
    model = EquipmentItem


@admin.register(CommunicationEquipmentDeclaration)
class CommunicationEquipmentDeclarationAdmin(admin.ModelAdmin):
    inlines = [EquipmentItemInline]
