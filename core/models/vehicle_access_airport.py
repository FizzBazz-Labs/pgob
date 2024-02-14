from django.db import models
from django.utils.translation import gettext as _

from core.models.country import Country


class VehicleTypes(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Vehicle(models.Model):

    def upload_file_name(self, filename):
        return f'vehicle/{self.accreditation_type}/{filename}'
    
    
    def create_image_path(self, filename: str):
        filename = filename.lower().replace(' ', '').replace('-', '')

        return f'vehicle/{self.id}/{filename}'


    # class VehicleTypes(models.TextChoices):
    #     CAR = 'Car', _('Car')
    #     PICK_UP = 'Pick up', _('Pick up')
    #     VAN = 'Van', _('Van')
    #     TRUCK = 'Truck', _('Truck')
    #     OTHER = 'Other', _('Other')

    vehicle_type = models.ManyToManyField(VehicleTypes, related_name='vehicle', blank=True)
    brand = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    license_plate = models.CharField(max_length=20)
    driver_name = models.CharField(max_length=150)
    driver_id = models.CharField(max_length=20)
    driver_phone = models.CharField(max_length=20)


class VehicleAccessAirport(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    vehicles = models.ManyToManyField(Vehicle, related_name='accreditations')

    responsible_info = models.CharField(max_length=150)
    responsible_signatures = models.TextField()
    date = models.DateField()
