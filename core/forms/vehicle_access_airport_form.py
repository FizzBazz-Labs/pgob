from django import forms

from core.models import VehicleAccessAirport


class VehicleAccessAirportForm(forms.ModelForm):
    class Meta:
        model = VehicleAccessAirport
        fields = '__all__'
