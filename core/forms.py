from django import forms


class NationalAccreditationForm(forms.Form):
    # Personal Data
    first_name = forms.CharField(label='Name', max_length=120)
    last_name = forms.CharField(label='Last Name', max_length=120)
