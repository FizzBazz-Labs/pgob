from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from core.models import AccreditationStatus


def image_filename(instance, filename: str):
    filename = filename.lower().replace(' ', '').replace('-', '')
    return f'internationals/{instance.first_name}_{instance.last_name}/{filename}'


def authorization_letter_filename(instance, filename: str):
    return f'internationals/{instance.first_name}_{instance.last_name}/authorizations/{filename}'


def passport_image_filename(instance, filename: str):
    return f'internationals/{instance.first_name}_{instance.last_name}/passport/{filename}'


def qr_filename(instance, filename: str):
    fullname = f'{instance.first_name.lower()}_{instance.last_name.lower()}'
    filename = filename.lower().replace(' ', '').replace('-', '')

    return f'nationals/{fullname}/qr/{filename}'


class InternationalAccreditation(models.Model):
    class AccreditationType(models.TextChoices):
        OFFICIAL_DELEGATION_HEAD = 'OFFICIAL_DELEGATION_HEAD', _(
            'Jefe de Delegación Oficial'),
        OFFICIAL_DELEGATION = 'OFFICIAL_DELEGATION', _('Delegación Oficial')
        PROTOCOL = 'PROTOCOL', _('Protocolo')
        SECURITY = 'SECURITY', _('Seguridad')
        SUPPORT_STAFF = 'SUPPORT_STAFF', _('Personal de Apoyo')
        OFFICIAL_NEWSLETTER = 'OFFICIAL_NEWSLETTER', _('Prensa Oficial')
        CREW = 'CREW', _('Tripulación')
        COMMERCIAL_NEWSLETTER = 'COMMERCIAL_NEWSLETTER', _('Prensa Comercial')

    country = models.ForeignKey(
        'countries.Country',
        on_delete=models.PROTECT,
        related_name='international_forms')

    # Personal Data
    image = models.ImageField(upload_to=image_filename)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    passport_id = models.CharField(max_length=150)
    passport_id_image = models.ImageField(
        blank=True, null=True,
        upload_to=passport_image_filename)
    private_insurance = models.CharField(max_length=150, blank=True)

    position = models.ForeignKey(
        'positions.Position',
        on_delete=models.PROTECT,
        related_name='international_forms')
    sub_position = models.ForeignKey(
        'positions.SubPosition',
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='international_forms')
    media_channel = models.ForeignKey(
        'media_channels.MediaChannel',
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='international_forms')
    authorization_letter = models.FileField(
        upload_to=authorization_letter_filename,
        blank=True)

    institution = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=150)
    phone_number_2 = models.CharField(max_length=150, blank=True)
    email = models.EmailField()
    birthday = models.DateField()
    birthplace = models.CharField(max_length=150)

    security_weapon_accreditation = models.ForeignKey(
        'security_accreditations.SecurityWeaponAccreditation',
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='international_forms')

    # Medical Information
    blood_type = models.CharField(max_length=150, blank=True)
    diseases = models.TextField(blank=True)
    medication_1 = models.CharField(max_length=200, blank=True)
    medication_2 = models.CharField(max_length=200, blank=True)
    medication_3 = models.CharField(max_length=200, blank=True)
    medication_4 = models.CharField(max_length=200, blank=True)
    allergies = models.ManyToManyField(
        'allergies.Allergy',
        related_name='international_forms',
        blank=True)
    allergies_description = models.TextField(blank=True, null=True)
    immunizations = models.ManyToManyField(
        'immunizations.Immunization',
        related_name='international_forms',
        blank=True)
    medicals = models.ManyToManyField(
        'medical_histories.MedicalHistory',
        related_name='international_forms',
        blank=True)
    surgical = models.CharField(max_length=150, blank=True)
    doctor_name = models.CharField(max_length=100, blank=True)

    # Hotel Information
    hotel_name = models.CharField(max_length=120)
    hotel_address = models.CharField(max_length=120)
    hotel_phone = models.CharField(max_length=120)

    # Flight Information
    flight_arrival_datetime = models.DateTimeField(blank=True, null=True)
    flight_arrival_number = models.CharField(max_length=150, blank=True)
    flight_arrival_airport = models.CharField(max_length=150, blank=True)
    flight_from = models.ForeignKey(
        'countries.Country',
        on_delete=models.PROTECT,
        related_name='flight_from',
        blank=True, null=True)

    flight_departure_datetime = models.DateTimeField(blank=True, null=True)
    flight_departure_number = models.CharField(max_length=150, blank=True)
    flight_departure_airport = models.CharField(max_length=150, blank=True)
    flight_to = models.ForeignKey(
        'countries.Country',
        on_delete=models.PROTECT,
        related_name='flight_to',
        blank=True, null=True)

    # Accreditation Type
    type = models.CharField(
        max_length=150,
        choices=AccreditationType.choices,
        verbose_name=_('Tipo de Acreditación'),
        null=True, blank=True)

    reviewed_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='international_reviewed_set')
    reviewed_comment = models.TextField(blank=True, null=True)

    authorized_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='international_authorized_set')
    authorized_comment = models.TextField(blank=True, null=True)

    rejected_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        blank=True, null=True,
        related_name='international_rejected_set')

    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='international_forms')

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
        return f'{self.first_name} - {self.last_name} - {self.country.name}'
