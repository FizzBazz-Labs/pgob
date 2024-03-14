from django.db import models
from django.utils.translation import gettext_lazy as _


class Equipment(models.Model):

    brand = models.CharField(
        max_length=150, verbose_name=_('Marca'), blank=True)
    model = models.CharField(
        max_length=150, verbose_name=_('Modelo'), blank=True)
    type = models.CharField(max_length=150, verbose_name=_('Tipo'))
    serial = models.CharField(
        max_length=150, verbose_name=_('Serial No.'), blank=True)
    frequency = models.CharField(
        max_length=150, verbose_name=_('Frecuencia'), blank=True)

    value = models.DecimalField(
        decimal_places=2, max_digits=15, verbose_name=_('Valor'), blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.type} - {self.serial}'
