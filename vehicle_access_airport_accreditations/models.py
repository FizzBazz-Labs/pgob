from django.db import models


class VehicleAccessAirportAccreditations(models.Model):
    country = models.ForeignKey('countries.Country', on_delete=models.CASCADE,
                                related_name='vehicle_access_airport_accreditations')
    information_responsible = models.CharField(max_length=150)
    vehicles = models.ManyToManyField(
        'vehicles.Vehicle', related_name='vehicle_access_airport_accreditations')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.country.name} - {self.information_responsible}'
