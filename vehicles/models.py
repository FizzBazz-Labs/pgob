from django.db import models


class Vehicle(models.Model):
    type = models.CharField(max_length=150)
    brand = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    plate = models.CharField(max_length=50)
    driver_name = models.CharField(max_length=150)
    driver_id = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.type} {self.brand}'
