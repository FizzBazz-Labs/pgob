from django.contrib import admin

from core.models import SiteConfiguration, Accreditation, Certification


@admin.register(Accreditation)
class AccreditationAdmin(admin.ModelAdmin):
    ...


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    ...


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
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
