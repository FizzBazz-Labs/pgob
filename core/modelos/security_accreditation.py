from django.db import models
from django.utils.translation import gettext as _

from core.models import Position, Nationality, Country, MediaChannel



class WeaponType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CommunicationType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SecurityAccreditation(models.Model):

    def upload_file_name(self, filename):
        return f'security_accreditation/{self.accreditation_type}/{filename}'
    
    
    def create_image_path(self, filename: str):
        filename = filename.lower().replace(' ', '').replace('-', '')

        return f'security_accreditation/{self.id}/{filename}'
    
    # class WeaponType(models.TextChoices):
    #      PISTOL = 'Pistol', _('Pistol')
    #      RIFLE = 'Rifle', _('Rifle')
    #      SHOTGUN = 'Shotgun', _('Shotgun')
    #      OTHER = 'Other', _('Other')

    # class CommunicationType(models.TextChoices):
    #      RADIO = 'Radio', _('Radio')
    #      OTHER = 'Other', _('Other')

    date_control = models.DateField()
    time_control = models.TimeField()
    disclaimer_accepted = models.BooleanField(default=False)
    
    # Weapon data
    #preguntar que va en weapon
    #arama blanca o de fuego
    weapon = models.CharField(max_length=150)
    brand = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    weapon_type = models.ManyToManyField(WeaponType, related_name='security_accreditation', blank=True)

    #weapon_type = models.CharField(max_length=50, choices=WeaponType.choices, null=True, default='default_value')

    serial_number = models.CharField(max_length=150)
    caliber = models.CharField(max_length=150)
    magazine_quantity = models.IntegerField()
    ammunition_quantity = models.IntegerField()

    # Communication equipment data
    #preguntar que va en radio y tipo
    communication_radio = models.CharField(max_length=150)
    communication_model = models.CharField(max_length=150)
    communication_type = models.ManyToManyField(CommunicationType, related_name='security_accreditation', blank=True)
    
    #communication_type = models.CharField(max_length=50, choices=CommunicationType.choices, null=True, default='default_value')
    
    communication_serial = models.CharField(max_length=150)
    communication_frequency = models.CharField(max_length=150)