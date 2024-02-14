from django.db import models
from django.utils.translation import gettext as _


class CommunicationEquipmentDeclaration(models.Model):
    country = models.ForeignKey('countries.Country', on_delete=models.CASCADE)
    institution_or_media = models.CharField(max_length=150)


class EquipmentItem(models.Model):
    declaration = models.ForeignKey(
        CommunicationEquipmentDeclaration,
        on_delete=models.CASCADE,
        related_name='equipments')
    object_type = models.CharField(max_length=50)
    brand = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    serial_number = models.CharField(max_length=150)
    approximate_value = models.IntegerField()
