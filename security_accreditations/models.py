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
    caliber = models.CharField(max_length=150, default='9mm', blank=True)
    chargers = models.IntegerField(verbose_name=_('Cantidad de Cargadores'))
    ammunition = models.IntegerField(verbose_name=_('Total de Municiones'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.weapon} - {self.caliber}'


def get_declaration_country(instance, filename: str):
    filename = filename.lower().replace(' ', '').replace('-', '')
    return f'security_weapons/{instance.country.name}/{instance.name}/{filename}'


class SecurityWeaponAccreditation(models.Model):
    country = models.ForeignKey(
        'countries.Country',
        on_delete=models.CASCADE,
        related_name='security_weapons',
        blank=True, null=True)

    name = models.TextField(blank=True, null=True)
    passport_id = models.TextField(blank=True, null=True)
    position = models.ForeignKey(
        'positions.Position',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='security_weapons')

    control_datetime = models.DateTimeField(
        verbose_name=_('Fecha y hora de Control'))

    # Weapon data
    weapons = models.ManyToManyField(
        'security_accreditations.Weapon',
        related_name='security_weapons',
        blank=True)

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

    reviewed_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='security_reviewed_set')
    reviewed_comment = models.TextField(blank=True)

    authorized_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='security_authorized_set')

    rejected_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='security_rejected_set')

    status = models.CharField(
        max_length=150,
        choices=AccreditationStatus.choices,
        default=AccreditationStatus.PENDING)

    certificated = models.BooleanField(default=False)
    certification = models.FileField(
        upload_to=get_declaration_country, blank=True, null=True)
    reviewed_comment = models.TextField(blank=True, null=True)
    authorized_comment = models.TextField(blank=True, null=True)
    uuid = models.TextField(blank=True)

    flight_arrival_datetime = models.DateTimeField(blank=True, null=True)
    flight_arrival_number = models.TextField(blank=True, null=True)
    flight_arrival_airport = models.TextField(blank=True, null=True)
    flight_departure_datetime = models.DateTimeField(blank=True, null=True)
    flight_departure_number = models.TextField(blank=True, null=True)
    flight_departure_airport = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    downloaded = models.BooleanField(default=False)
    permit_number = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f'{self.control_datetime} - {self.created_by}'
