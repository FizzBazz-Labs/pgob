from django.contrib import admin
from django.db import models
from django import forms
from django.utils.translation import gettext as _

from core.models import *


@admin.register(CommunicationEquipmentDeclaration)
class CommunicationEquipmentDeclarationAdmin(admin.ModelAdmin):
    ...


@admin.register(EquipmentItem)
class EquipmentItemAdmin(admin.ModelAdmin):
    ...
