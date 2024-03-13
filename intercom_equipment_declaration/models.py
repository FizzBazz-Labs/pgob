from django.db import models
from django.contrib.auth import get_user_model

from core.models import AccreditationStatus


class IntercomEquipmentDeclaration(models.Model):
    country = models.ForeignKey('countries.Country', on_delete=models.CASCADE,
                                related_name='intercom_equipment_declarations')
    institution = models.CharField(max_length=150)
    equipments = models.ManyToManyField(
        'equipments.Equipment', related_name='intercom_equipment_declarations', blank=True)
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='intercom_equipment_declarations')

    reviewed_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='communication_equipment_reviewed_set')

    authorized_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='communication_equipment_authorized_set')

    rejected_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='communication_equipment_rejected_set')

    status = models.CharField(
        max_length=150,
        choices=AccreditationStatus.choices,
        default=AccreditationStatus.PENDING)

    def __str__(self):
        return f'{self.country.name} - {self.institution}'
