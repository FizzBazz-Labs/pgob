from django.db import models
from django.utils.translation import gettext_lazy as _


class SiteConfiguration(models.Model):
    available = models.BooleanField(default=True)

    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='site/logo', null=True, blank=True)
    favicon = models.ImageField(upload_to='site/favicon', null=True, blank=True)

    # Login Background
    login_background = models.ImageField(upload_to='site/backgrounds', null=True, blank=True)

    # Unavailable Site
    unavailable_title = models.CharField(max_length=255, default='Sitio en Mantenimiento')
    unavailable_message = models.TextField(
        blank=True,
        default='Estamos realizando tareas de mantenimiento. Por favor, vuelva más tarde.')
    unavailable_color = models.CharField(max_length=15, blank=True, default='#000000')
    unavailable_background = models.ImageField(upload_to='site/backgrounds', null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class AccreditationStatus(models.TextChoices):
    PENDING = 'PENDING', _('Pending')
    REVIEWED = 'REVIEWED', _('Reviewed')
    APPROVED = 'APPROVED', _('Approved')
    REJECTED = 'REJECTED', _('Rejected')


class Accreditation(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
