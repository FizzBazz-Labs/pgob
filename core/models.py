from django.db import models
from django.utils.translation import gettext_lazy as _


class STATUS(models.TextChoices):
    PENDING = 'PENDING', _('Pendiente')
    APPROVED = 'APPROVED', _('Aprobado')
    REJECTED = 'REJECTED', _('Rechazado')
