from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from core.models import *


@receiver(post_save, sender=NationalAccreditation)
def post_save_na(sender, instance: NationalAccreditation, **kwargs):
    email = EmailMessage(
        subject='Nuevo Registro | Acreditación Nacional',
        to=['rodriguez.garcia.allan@gmail.com'],
        body=render_to_string(
            'notifications/emails/na/new.html',
            {'item': instance},
        ),
    )

    email.content_subtype = 'html'
    email.send()
