from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class VehicleAccessAirport(models.Model):
    country = models.ForeignKey(
        'countries.Country',
        on_delete=models.CASCADE,
        related_name='vehicle_forms')

    responsible = models.CharField(max_length=150)
    signature = models.TextField()

    date = models.DateField()

    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='general_vehicle_forms')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Vehicle(models.Model):
    type = models.CharField(max_length=150)
    brand = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    plate = models.CharField(max_length=20)

    driver_name = models.CharField(max_length=150)
    driver_id = models.CharField(max_length=20)
    driver_phone = models.CharField(max_length=20)

    accreditation = models.ForeignKey(
        'core.VehicleAccessAirport',
        on_delete=models.CASCADE,
        related_name='vehicles')
