from django.db import models
from django.utils.translation import gettext as _

from core.models import Position, Nationality, Country, MediaChannel

class GeneralVehicleAccreditation(models.Model):


    def upload_file_name(self, filename):
        return f'general_vehicle_accreditation/{self.accreditation_type}/{filename}'
    
    
    def create_image_path(self, filename: str):
        filename = filename.lower().replace(' ', '').replace('-', '')

        return f'general_vehicle_accreditation/{self.id}/{filename}'

    
    mission = models.TextField()
    vehicle_brand = models.CharField(max_length=150)
    license_plate = models.CharField(max_length=20)
    color = models.CharField(max_length=150)
    driver_name = models.CharField(max_length=150)
    dip = models.CharField(max_length=150)
    assigned = models.TextField()
    
    distinctive = models.CharField(max_length=150)
    observations = models.TextField()

    responsible_signatures = models.TextField()
    date = models.DateField()