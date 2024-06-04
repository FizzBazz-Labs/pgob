from django.db import models


class HelpSection(models.Model):
    title = models.CharField(max_length=255)
    accreditations = models.ManyToManyField('core.Accreditation')

    def __str__(self) -> str:
        return self.title


class HelpSectionItem(models.Model):
    title = models.CharField(max_length=255)
    url = models.FileField(upload_to='helps/', blank=True)
    groups = models.ManyToManyField('auth.Group')
    section = models.ForeignKey(
        HelpSection,
        on_delete=models.CASCADE,
        related_name='items')

    def __str__(self) -> str:
        return self.title
