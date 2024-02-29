from django.db import models


class IntercomEquipmentDeclaration(models.Model):
    country = models.ForeignKey('countries.Country', on_delete=models.CASCADE,
                                related_name='intercom_equipment_declarations')
    institution = models.CharField(max_length=150)
    equipments = models.ManyToManyField(
        'equipments.Equipment', related_name='intercom_equipment_declarations', blank=True)

    def __str__(self):
        return f'{self.country.name} - {self.institution}'
