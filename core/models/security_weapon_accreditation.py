from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class SecurityWeaponAccreditation(models.Model):
    accreditation = models.ForeignKey(
        'core.InternationalAccreditation',
        on_delete=models.CASCADE,
        related_name='weapons')
    control_date = models.DateField()
    control_time = models.TimeField()

    # Weapon data
    weapon = models.CharField(max_length=150)
    brand = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    type = models.CharField(max_length=150)
    serial = models.CharField(max_length=150)
    caliber = models.CharField(max_length=150)
    chargers = models.IntegerField()
    ammunition = models.IntegerField()

    # Communication Data
    equipment_radio = models.CharField(max_length=150)
    equipment_model = models.CharField(max_length=150)
    equipment_type = models.CharField(max_length=150)
    equipment_serial = models.CharField(max_length=150)
    equipment_frequency = models.CharField(max_length=150)

    observations = models.TextField(blank=True)

    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='weapon_forms')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
