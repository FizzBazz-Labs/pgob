from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class GeneralVehicleAccreditation(models.Model):
    mission = models.TextField()
    brand = models.CharField(max_length=150)
    plate = models.CharField(max_length=20)
    color = models.CharField(max_length=150)
    driver = models.CharField(max_length=150)
    dip = models.CharField(max_length=150)
    assigned = models.TextField()

    distinctive = models.CharField(max_length=150)
    observations = models.TextField()

    signature = models.TextField()
    date = models.DateField()

    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='general_vehicle_forms')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
