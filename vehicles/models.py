from django.db import models


def driver_license_filename(instance, filename: str):
    filename = filename.lower().replace(' ', '').replace('-', '')
    return f'driver_licenses/{instance.driver_id}/{filename}'


def tpv_filename(instance, filename: str):
    filename = filename.lower().replace(' ', '').replace('-', '')
    return f'circulation_cards/{instance.driver_id}/{filename}'


class Vehicle(models.Model):
    type = models.CharField(max_length=150)
    type_other = models.CharField(max_length=150, blank=True)
    brand = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    plate = models.CharField(max_length=50)
    driver_name = models.CharField(max_length=150)
    driver_id = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, blank=True)
    driver_license = models.FileField(
        upload_to=driver_license_filename,
        blank=True, null=True)
    tpv = models.FileField(
        upload_to=tpv_filename,
        blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.type} {self.brand}'
