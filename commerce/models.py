from django.db import models
from django.contrib.auth import get_user_model

from core.models import AccreditationStatus


def qr_filename(instance, filename: str):
    fullname = f'{instance.first_name.lower()}_{instance.last_name.lower()}'
    filename = filename.lower().replace(' ', '').replace('-', '')

    return f'commerce/{fullname}/qr/{filename}'


class Commerce(models.Model):
    class CommerceType(models.TextChoices):
        factory = 'FACTORY', 'Factory'
        store = 'STORE', 'Store'
        supermarket = 'SUPERMARKET', 'Supermarket'
        local = 'LOCAL', 'Local'
        square = 'SQUARE', 'Square'
        other = 'OTHER', 'Other'

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    passport_id = models.CharField(max_length=100)
    country = models.ForeignKey('countries.Country', on_delete=models.PROTECT)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    admin_name = models.CharField(max_length=150, blank=True)
    admin_phone_number = models.CharField(max_length=150, blank=True)
    commerce_type = models.CharField(max_length=150)
    commerce_type_other = models.CharField(max_length=150, blank=True)

    has_vehicle = models.BooleanField(default=False)
    vehicle_type = models.CharField(max_length=150, blank=True)
    vehicle_type_other = models.CharField(max_length=150, blank=True)
    vehicle_plate = models.CharField(max_length=150, blank=True)
    vehicle_color = models.CharField(max_length=150, blank=True)
    vehicle_year = models.CharField(max_length=150, blank=True)
    vehicle_model = models.CharField(max_length=150, blank=True)

    downloaded = models.BooleanField(default=False)

    reviewed_comment = models.TextField(blank=True)
    reviewed_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='commerce_reviewed_set',
        blank=True, null=True)

    authorized_comment = models.TextField(blank=True)
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

    status = models.CharField(
        max_length=150,
        choices=AccreditationStatus.choices,
        default=AccreditationStatus.PENDING)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    uuid = models.TextField(blank=True)
    qr_code = models.ImageField(upload_to=qr_filename, blank=True)
