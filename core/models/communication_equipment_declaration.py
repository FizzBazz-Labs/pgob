from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class CommunicationEquipmentDeclaration(models.Model):
    country = models.ForeignKey(
        'countries.Country',
        on_delete=models.PROTECT,
        related_name='equipment_forms')
    institution_or_media = models.CharField(max_length=150)

    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='equipment_forms')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class EquipmentItem(models.Model):
    declaration = models.ForeignKey(
        'core.CommunicationEquipmentDeclaration',
        on_delete=models.CASCADE,
        related_name='equipments')
    object_type = models.CharField(max_length=50)
    brand = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    serial_number = models.CharField(max_length=150)
    approximate_value = models.IntegerField()
