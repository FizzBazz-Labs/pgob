from django.db import models
from django.contrib.auth import get_user_model

from accreditations.models import Accreditation


class Commerce(Accreditation):
    class CommerceType(models.TextChoices):
        factory = 'FACTORY', 'Factory'
        store = 'STORE', 'Store'
        supermarket = 'SUPERMARKET', 'Supermarket'
        local = 'LOCAL', 'Local'
        square = 'SQUARE', 'Square'
        other = 'OTHER', 'Other'

    commercial_name = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    admin_name = models.CharField(max_length=150, blank=True)
    admin_phone_number = models.CharField(max_length=150, blank=True)
    commerce_type = models.CharField(max_length=150)
    commerce_type_other = models.CharField(max_length=150, blank=True)
    vehicles = models.ManyToManyField('vehicles.Vehicle', blank=True)

    reviewed_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='commerce_reviewed_set',
        blank=True, null=True)
    authorized_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='commerce_authorized_set',
        blank=True, null=True)
    rejected_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='commerce_rejected_set',
        blank=True, null=True)
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='commerce_created_set')


class CommerceEmployee(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    passport_id = models.CharField(max_length=100)
    country = models.ForeignKey('countries.Country', on_delete=models.PROTECT)
    birthday = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    schedule = models.CharField(max_length=150, blank=True)
    commerce = models.ForeignKey(Commerce, on_delete=models.CASCADE, related_name='employees')
