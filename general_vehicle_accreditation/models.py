from django.db import models
from django.contrib.auth import get_user_model


class GeneralVehicleAccreditation(models.Model):
    mission = models.CharField(max_length=150)
    assigned_to = models.CharField(max_length=150)
    vehicles = models.ManyToManyField(
        'vehicles.Vehicle', related_name='general_vehicle_accreditations')
    distinctive = models.CharField(max_length=150, blank=True)
    observations = models.CharField(max_length=150, blank=True)
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='general_vehicle_accreditations')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.mission} - {self.assigned_to}'
