from django.db import models
from django.contrib.auth import get_user_model

from core.models import AccreditationStatus


def get_declaration_country(instance, filename: str):
    filename = filename.lower().replace(' ', '').replace('-', '')
    return f'intercom_equipment_declaration/{instance.country.name}/{instance.institution}/{filename}'


class IntercomEquipmentDeclaration(models.Model):
    country = models.ForeignKey(
        'countries.Country',
        on_delete=models.CASCADE,
        related_name='intercom_equipment_declarations')
    institution = models.CharField(max_length=150)
    equipments = models.ManyToManyField(
        'equipments.Equipment',
        related_name='intercom_equipment_declarations',
        blank=True)
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='intercom_equipment_declarations')

    reviewed_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='communication_equipment_reviewed_set')
    # reviewed_comment = models.TextField(blank=True)

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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    certificated = models.BooleanField(default=False)
    certification = models.FileField(
        upload_to=get_declaration_country, blank=True, null=True)
    reviewed_comment = models.TextField(blank=True, null=True)
    authorized_comment = models.TextField(blank=True, null=True)
    uuid = models.TextField(blank=True)

    def __str__(self):
        return f'{self.country.name} - {self.institution}'
