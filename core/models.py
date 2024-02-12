from django.db import models
from django.utils.translation import gettext as _


def create_image_path(instance, filename: str):
    filename = filename.lower().replace(' ', '').replace('-', '')

    return f'nationalacreditaion/files/{instance.id}/{filename}'

#co
class Country(models.Model):
    name = models.CharField(max_length=150)


class Nationality(models.Model):
    name = models.CharField(max_length=150)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    

class Position(models.Model):
    name = models.CharField(max_length=150)
    
    
class MediaChannel(models.Model):
    name = models.CharField(max_length=120)



class CommunicationEquipmentDeclaration(models.Model):
    country_name = models.ForeignKey(Country, on_delete=models.CASCADE)
    institution_or_media = models.CharField(max_length=150)


class EquipmentItem(models.Model):
    declaration = models.ForeignKey(CommunicationEquipmentDeclaration, on_delete=models.CASCADE, related_name='equipments')
    object_type = models.CharField(max_length=50)
    brand = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    serial_number = models.CharField(max_length=150)
    approximate_value = models.IntegerField()   





