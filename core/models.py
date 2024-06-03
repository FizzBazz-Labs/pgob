from django.db import models
from django.utils.translation import gettext_lazy as _


class SiteConfiguration(models.Model):
    available = models.BooleanField(default=True)

    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='site/logo', null=True, blank=True)
    favicon = models.ImageField(
        upload_to='site/favicon', null=True, blank=True)

    # Login Background
    login_background = models.ImageField(
        upload_to='site/backgrounds', null=True, blank=True)
    login_title = models.CharField(max_length=255, default='Iniciar Sesión')
    login_title_2 = models.CharField(max_length=255, default='Acreditaciones')
    login_title_3 = models.CharField(
        max_length=255, default='Acreditaciones', null=True, blank=True)
    login_title_color = models.CharField(max_length=150, default='#FFFFFF')
    use_bold = models.BooleanField(default=True)
    login_title_size = models.CharField(max_length=150, default='24')

    # Unavailable Site
    unavailable_title = models.CharField(
        max_length=255, default='Sitio en Mantenimiento')
    unavailable_message = models.TextField(
        blank=True,
        default='Estamos realizando tareas de mantenimiento. Por favor, vuelva más tarde.')
    unavailable_color = models.CharField(
        max_length=15, blank=True, default='#000000')
    unavailable_background = models.ImageField(
        upload_to='site/backgrounds', null=True, blank=True)

    # President
    president = models.CharField(
        max_length=255, default='Nombre del Presidente/a')
    term_date = models.DateField(default='2024-12-31')

    def __str__(self) -> str:
        return self.name


class AccreditationStatus(models.TextChoices):
    PENDING = 'PENDING', _('Pendiente')
    REVIEWED = 'REVIEWED', _('Revisado')
    APPROVED = 'APPROVED', _('Aprobado')
    REJECTED = 'REJECTED', _('Rechazado')


class Accreditation(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Certification(models.Model):
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
        OFFICIAL_DELEGATION_HEAD = 'OFFICIAL_DELEGATION_HEAD', _(
            'Jefe de Delegación Oficial'),
        SUPPORT_STAFF = 'SUPPORT_STAFF', _('Personal de Apoyo')
        OFFICIAL_NEWSLETTER = 'OFFICIAL_NEWSLETTER', _('Prensa Oficial')
        CREW = 'CREW', _('Tripulación')

    accreditation_type = models.CharField(
        max_length=150,
        choices=AccreditationType.choices,
        default=AccreditationType.GENERAL_COORDINATION)
    color = models.CharField(max_length=150)
    text_color = models.CharField(max_length=150, default='#FFFFFF')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        accreditation_type = self.AccreditationType(self.accreditation_type)

        return str(accreditation_type.label)


class Report(models.Model):
    name = models.CharField(max_length=255)
    report_id = models.CharField(max_length=255)
    dataset_id = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.report_id


class PowerBiToken(models.Model):
    token = models.TextField()
    expiration_date = models.DateTimeField()
    access_token = models.TextField()

    def __str__(self) -> str:
        return f'token {self.pk}'
