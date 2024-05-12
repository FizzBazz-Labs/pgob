from django.db import models
from django.contrib.auth import get_user_model

from accreditations.models import Accreditation


class Housing(Accreditation):
    class BuildingType(models.TextChoices):
        house = 'HOUSE', 'House'
        apartment = 'APARTMENT', 'Apartment'

    address = models.CharField(max_length=150)
    building_type = models.CharField(max_length=150, choices=BuildingType.choices)
    house_number = models.CharField(max_length=150, blank=True)
    apartment_tower = models.CharField(max_length=150, blank=True)
    building_admin_name = models.CharField(max_length=150, blank=True)
    apartment_number = models.CharField(max_length=150, blank=True)
    apartment_floor = models.CharField(max_length=150, blank=True)
    is_owner = models.BooleanField(default=False)
    owner_name = models.CharField(max_length=150, blank=True)
    owner_phone_number = models.CharField(max_length=150, blank=True)
    vehicles = models.ManyToManyField('vehicles.Vehicle', blank=True)

    reviewed_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='housing_reviewed_set',
        blank=True, null=True)
    authorized_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='housing_authorized_set',
        blank=True, null=True)
    rejected_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='housing_rejected_set',
        blank=True, null=True)
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='housing_created_set')


class HousingPerson(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    passport_id = models.CharField(max_length=100)
    country = models.ForeignKey('countries.Country', on_delete=models.PROTECT)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=150)
    email = models.EmailField()
    housing = models.ForeignKey(Housing, on_delete=models.CASCADE, related_name='persons')
