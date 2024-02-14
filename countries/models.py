from django.db import models
from django.utils.translation import gettext as _


class Country(models.Model):
    name = models.CharField(max_length=150)
    nationality = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = _('countries')
