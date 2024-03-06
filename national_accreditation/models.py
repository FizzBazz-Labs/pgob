from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _

from core.models import AccreditationStatus


def image_filename(instance, filename: str):
    fullname = f'{instance.first_name.lower()}_{instance.last_name.lower()}'
    filename = filename.lower().replace(' ', '').replace('-', '')

    return f'nationals/{fullname}/{filename}'


def authorization_letter_filename(instance, filename: str):
    fullname = f'{instance.first_name.lower()}_{instance.last_name.lower()}'
    filename = filename.lower().replace(' ', '').replace('-', '')

    return f'nationals/{fullname}/authorizations/{filename}'


class NationalAccreditation(models.Model):
    class AccreditationType(models.TextChoices):
        GENERAL_COORDINATION = (
            'GENERAL_COORDINATION',
            _('Coordinación General'),
        )
        PROTOCOL = 'PROTOCOL', _('Protocolo')
        SECURITY = 'SECURITY', _('Seguridad')
        TECHNICAL_STAFF = 'TECHNICAL_STAFF', _('Personal Técnico')
        OFFICIAL_DELEGATION = 'Delegación Oficial', _('Delegación Oficial')
        LINK = 'LINK', _('Enlace')
        SUPPLIER = 'SUPPLIER', _('Proveedor')
        NEWSLETTER_COMMITTEE = 'NEWSLETTER_COMMITTEE', _('Comisión de Prensa')
        COMMERCIAL_NEWSLETTER = 'COMMERCIAL_NEWSLETTER', _('Prensa Comercial')

    class BloodType(models.TextChoices):
        A_POSITIVE = 'A+', _('A+')
        A_NEGATIVE = 'A-', _('A-')
        B_POSITIVE = 'B+', _('B+')
        B_NEGATIVE = 'B-', _('B-')
        O_POSITIVE = 'O+', _('O+')
        O_NEGATIVE = 'O-', _('O-')
        AB_POSITIVE = 'AB+', _('AB+')
        AB_NEGATIVE = 'AB-', _('AB-')

    image = models.ImageField(upload_to=image_filename)
    first_name = models.CharField(max_length=150, verbose_name=_('Nombre'))
    last_name = models.CharField(max_length=150, verbose_name=_('Apellido'))
    passport_id = models.CharField(
        max_length=100, verbose_name=_('Cédula /Pasaporte'))

    position = models.ForeignKey(
        'positions.Position',
        on_delete=models.PROTECT,
        verbose_name=_('Cargo en el Evento'),
        related_name='national_forms')
    sub_position = models.ForeignKey(
        'positions.SubPosition',
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='national_forms')
    media_channel = models.ForeignKey(
        'media_channels.MediaChannel',
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='national_forms')
    authorization_letter = models.FileField(
        upload_to=authorization_letter_filename,
        blank=True)

    security_weapon_accreditation = models.ForeignKey(
        'security_accreditations.SecurityWeaponAccreditation',
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='national_forms')

    institution = models.CharField(
        max_length=150, verbose_name=_('Institución'))
    address = models.CharField(max_length=150, verbose_name=_('Dirección'))
    phone_number = models.CharField(max_length=150, verbose_name=_('Teléfono'))
    phone_number_2 = models.CharField(
        max_length=150, blank=True, verbose_name=_('Teléfono 2'))
    email = models.EmailField(verbose_name=_('Correo Electrónico'))
    birthday = models.DateField(verbose_name=_('Fecha de Nacimiento'))
    birthplace = models.CharField(
        max_length=250, verbose_name=_('Lugar de Nacimiento'))
    blood_type = models.CharField(
        max_length=150, choices=BloodType.choices, verbose_name=_('Tipo de Sangre'))

    # Accreditation Type
    type = models.CharField(
        max_length=150,
        choices=AccreditationType.choices,
        verbose_name=_('Tipo de Acreditación'))

    # Todo: Move to Many to Many
    authorized_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='national_forms_verifies',
        verbose_name=_('Creado por'))

    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='national_forms',
        verbose_name=_('Creado por'))

    status = models.CharField(
        max_length=150,
        choices=AccreditationStatus.choices,
        default=AccreditationStatus.PENDING)

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Creado el'))
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Acreditación | {self.first_name} {self.last_name}'
