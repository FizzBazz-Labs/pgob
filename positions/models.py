from django.db import models
from django.utils.translation import gettext_lazy as _


class Position(models.Model):
    name = models.CharField(max_length=250)


class SubPosition(models.Model):
    position = models.ForeignKey(
        'positions.Position',
        on_delete=models.CASCADE,
        related_name='sub_positions')
    name = models.CharField(max_length=250)
