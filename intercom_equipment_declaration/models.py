from django.db import models
from django.contrib.auth import get_user_model

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
    
    def __str__(self):
        return f'{self.country.name} - {self.institution}'
