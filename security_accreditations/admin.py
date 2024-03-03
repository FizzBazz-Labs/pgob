from django.contrib import admin

from security_accreditations.models import SecurityWeaponAccreditation


@admin.register(SecurityWeaponAccreditation)
class SecurityWeaponAccreditationAdmin(admin.ModelAdmin):
    ...
