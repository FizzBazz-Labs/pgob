from django.db import models
from django.utils.translation import gettext_lazy as _


class Position(models.Model):
    class NewsletterPosition(models.TextChoices):
        Cameraman = 'cameraman', _('Camarógrafo Oficial')
        Photographer = 'photographer', _('Fotógrafo Oficial')
        Technical = 'technical', _('Técnico/Apoyo')
        Journalist = 'journalist', _('Periodista')
        DigitalCommunicationsOfficer = (
            'digital_communications_officer',
            _('Oficial de Comunicación Digital'),
        )

    name = models.CharField(max_length=250)
    sub_position = models.CharField(
        max_length=150,
        choices=NewsletterPosition.choices,
        blank='')
