from django.db import models
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    name = models.CharField(max_length=150)
    nationality = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = _('countries')

    def __str__(self) -> str:
        return self.name

    @classmethod
    def get_default_pk(cls):
        branch, _ = cls.objects.get_or_create(
            name='Panamá',
            defaults={
                'nationality': 'Panameño'
            }
        )

        return branch.pk
