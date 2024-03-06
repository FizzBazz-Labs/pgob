from django.db import models
from django.utils.translation import gettext_lazy as _


class AccreditationStatus(models.TextChoices):
    PENDING = 'PENDING', _('Pendiente')
    REVIEWED = 'REVIEWED', _('Revisado')
    APPROVED = 'APPROVED', _('Aprobado')
    REJECTED = 'REJECTED', _('Rechazado')
