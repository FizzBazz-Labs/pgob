from django import forms

from core.models import GeneralVehicleAccreditation


class GeneralVehicleAccreditationForm(forms.ModelForm):
    class Meta:
        model = GeneralVehicleAccreditation
