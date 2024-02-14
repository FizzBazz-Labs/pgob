from django.db import models
from django.utils.translation import gettext_lazy as _


class Position(models.Model):
    name = models.CharField(max_length=250)
    sub_positions = models.ManyToManyField(
        'positions.SubPosition',
        related_name='positions')

    def __str__(self) -> str:
        return self.name


class SubPosition(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name
