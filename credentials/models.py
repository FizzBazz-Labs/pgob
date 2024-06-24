from django.db import models


class VehicleCertification(models.Model):
    name = models.CharField(max_length=250)
    color = models.CharField(max_length=150)
    text_color = models.CharField(max_length=150, default='#FFFFFF')

    def __str__(self):
        return self.name
