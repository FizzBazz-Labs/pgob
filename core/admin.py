from django.contrib import admin
from django import forms

from core.models import SiteConfiguration, Accreditation, Certification


@admin.register(Accreditation)
class AccreditationAdmin(admin.ModelAdmin):
    ...


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    ...


class SiteConfigForm(forms.ModelForm):
    class Meta:
        model = SiteConfiguration
        fields = '__all__'
        widgets = {
            'login_title_color': forms.TextInput(attrs={'type': 'color'}),
        }


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    form = SiteConfigForm

    fieldsets = (
        (None, {
            'fields': (
                'available',
            )
        }),
        ('General', {
            'fields': (
                'name',
                'logo',
                'favicon',
            )
        }),
        ('Login Background', {
            'fields': (
                'login_background',
                'login_title',
                'login_title_2',
                'login_title_3',
                'use_bold',
                'login_title_color',
                'login_title_size',
            )
        }),
        ('Unavailable Site', {
            'fields': (
                'unavailable_title',
                'unavailable_message',
                'unavailable_color',
                'unavailable_background',
            )
        }),
        ('President', {
            'fields': (
                'president',
                'term_date',
            )
        }),
    )
