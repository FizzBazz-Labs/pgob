from django.db import models
from django.utils.translation import gettext_lazy as _


class Accreditation(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', _('Pendiente')
        REVIEWED = 'REVIEWED', _('Revisado')
        APPROVED = 'APPROVED', _('Aprobado')
        REJECTED = 'REJECTED', _('Rechazado')

    certificated = models.BooleanField(default=False)
    certification = models.ImageField(upload_to='certifications/img/', blank=True, null=True)
    reviewed_comment = models.TextField(blank=True, null=True)
    authorized_comment = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=150, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uuid = models.TextField(blank=True)

    class Meta:
        abstract = True
        ordering = ['-updated_at']
