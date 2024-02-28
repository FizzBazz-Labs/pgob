from django import forms

from core.models import SecurityWeaponAccreditation


class SecurityWeaponAccreditationForm(forms.ModelForm):
    class Meta:
        model = SecurityWeaponAccreditation
        fields = '__all__'
