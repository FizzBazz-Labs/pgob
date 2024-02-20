from django import forms

from core.models import InternationalAccreditation
from allergies.models import Allergy


class InternationalAccreditationForm(forms.ModelForm):

    allergies = forms.ModelMultipleChoiceField(
        queryset=Allergy.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = InternationalAccreditation
        fields = [
            'country',
            'image',
            'first_name',
            'last_name',
            'passport_id',
            'position',
            'sub_position',
            'media_channel',
            'authorization_letter',
            'institution',
            'address',
            'phone_number',
            'phone_number_2',
            'email',
            'birthday',
            'birthplace',
            'blood_group',
            'blood_rh_factor',
            'age',
            'diseases',
            'medication_1',
            'medication_2',
            'medication_3',
            'medication_4',
            'allergies',
            'immunizations',
            'medicals',
            'surgical',
            'doctor_name',
            'hotel_name',
            'hotel_address',
            'hotel_phone',
            'flight_arrival_date',
            'flight_arrival_time',
            'flight_arrival_number',
            'flight_from',
            'flight_departure_date',
            'flight_departure_time',
            'flight_departure_number',
            'flight_to',
            'type',
            'authorized_by',
            'authorized_by_position',
            'created_by',
        ]
