from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

from core.models import AccreditationStatus

from countries.models import Country


def image_filename(instance, filename: str):
    fullname = f'{instance.first_name.lower()}_{instance.last_name.lower()}'
    filename = filename.lower().replace(' ', '').replace('-', '')

    return f'nationals/{fullname}/{filename}'


def authorization_letter_filename(instance, filename: str):
    fullname = f'{instance.first_name.lower()}_{instance.last_name.lower()}'
    filename = filename.lower().replace(' ', '').replace('-', '')

    return f'nationals/{fullname}/authorizations/{filename}'


def qr_filename(instance, filename: str):
    fullname = f'{instance.first_name.lower()}_{instance.last_name.lower()}'
    filename = filename.lower().replace(' ', '').replace('-', '')

    return f'nationals/{fullname}/qr/{filename}'


class NationalAccreditation(models.Model):
    class AccreditationType(models.TextChoices):
        GENERAL_COORDINATION = 'GENERAL_COORDINATION', _(
            'Coordinación General')
        PROTOCOL = 'PROTOCOL', _('Protocolo')
        SECURITY = 'SECURITY', _('Seguridad')
        TECHNICAL_STAFF = 'TECHNICAL_STAFF', _('Personal Técnico')
        OFFICIAL_DELEGATION = 'OFFICIAL_DELEGATION', _('Delegación Oficial')
        LINK = 'LINK', _('Enlace')
        SUPPLIER = 'SUPPLIER', _('Proveedor')
        NEWSLETTER_COMMITTEE = 'NEWSLETTER_COMMITTEE', _('Comisión de Prensa')
        COMMERCIAL_NEWSLETTER = 'COMMERCIAL_NEWSLETTER', _('Prensa Comercial')

    image = models.ImageField(upload_to=image_filename)
    first_name = models.CharField(max_length=150, verbose_name=_('Nombre'))

    country = models.ForeignKey(
        Country, on_delete=models.PROTECT)

    last_name = models.CharField(max_length=150, verbose_name=_('Apellido'))
    passport_id = models.CharField(
        max_length=100, verbose_name=_('Cédula /Pasaporte'))

    private_insurance = models.CharField(max_length=150, blank=True)

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

    # Medical Information
    blood_type = models.CharField(max_length=150, blank=True)
    diseases = models.TextField(blank=True)
    medication_1 = models.CharField(max_length=200, blank=True)
    medication_2 = models.CharField(max_length=200, blank=True)
    medication_3 = models.CharField(max_length=200, blank=True)
    medication_4 = models.CharField(max_length=200, blank=True)
    allergies = models.ManyToManyField(
        'allergies.Allergy',
        blank=True)
    allergies_description = models.TextField(blank=True, null=True)
    immunizations = models.ManyToManyField(
        'immunizations.Immunization',
        blank=True)
    medicals = models.ManyToManyField(
        'medical_histories.MedicalHistory',
        blank=True)
    surgical = models.CharField(max_length=150, blank=True)
    doctor_name = models.CharField(max_length=100, blank=True)

    # Accreditation Type
    type = models.CharField(
        max_length=150,
        choices=AccreditationType.choices,
        blank=True, null=True)

    reviewed_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='national_reviewed_set')
    reviewed_comment = models.TextField(blank=True, null=True)

    authorized_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='national_authorized_set')
    authorized_comment = models.TextField(blank=True, null=True)

    rejected_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='national_rejected_set')

    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='national_forms')

    status = models.CharField(
        max_length=150,
        choices=AccreditationStatus.choices,
        default=AccreditationStatus.PENDING)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    times_edited = models.PositiveIntegerField(default=0)

    uuid = models.TextField(blank=True)

    certificated = models.BooleanField(default=False)
    certification = models.ImageField(upload_to=qr_filename, blank=True)

    def __str__(self):
        return f'Acreditación | {self.first_name} {self.last_name}'
