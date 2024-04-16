from django.db import models


class Allergy(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Immunization(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class MedicalHistory(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class BloodType(models.TextChoices):
    A_POSITIVE = 'A+', _('A+')
    A_NEGATIVE = 'A-', _('A-')
    B_POSITIVE = 'B+', _('B+')
    B_NEGATIVE = 'B-', _('B-')
    O_POSITIVE = 'O+', _('O+')
    O_NEGATIVE = 'O-', _('O-')
    AB_POSITIVE = 'AB+', _('AB+')
    AB_NEGATIVE = 'AB-', _('AB-')
