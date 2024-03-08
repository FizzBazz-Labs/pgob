from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import AccreditationStatus


class Weapon(models.Model):
    weapon = models.CharField(max_length=150, verbose_name=_('Arma'))
    brand = models.CharField(max_length=150, verbose_name=_('Marca'))
    model = models.CharField(max_length=150, verbose_name=_('Modelo'))
    type = models.CharField(max_length=150, verbose_name=_('Tipo de Arma'))

    serial = models.CharField(max_length=150, verbose_name=_('Serial No.'))
    caliber = models.CharField(max_length=150, verbose_name=_('Calibre'))
    chargers = models.IntegerField(verbose_name=_('Cantidad de Cargadores'))
    ammunition = models.IntegerField(verbose_name=_('Total de Municiones'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.weapon} - {self.caliber}'


class SecurityWeaponAccreditation(models.Model):
    control_datetime = models.DateTimeField(
        verbose_name=_('Fecha y hora de Control'))

    # Weapon data
    weapons = models.ManyToManyField(
        'security_accreditations.Weapon', related_name='security_weapons', blank=True)

    communication_items = models.ManyToManyField(
        'equipments.Equipment',
        related_name='security_weapons',
        verbose_name=_('Elementos de Comunicación'),
        blank=True
    )

    observations = models.TextField(
        blank=True,
        verbose_name=_('Observaciones: (detallar otros elementos de protección y detención)'))

    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='sw_set')
    status = models.CharField(
        max_length=150,
        choices=AccreditationStatus.choices,
        default=AccreditationStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.control_datetime} - {self.created_by}'
