from typing import Any
from django import forms

from core.models import NationalAccreditation


class NationalAccreditationForm(forms.ModelForm):
    class Meta:
        model = NationalAccreditation
        fields = [
            'image',
            'first_name',
            'last_name',
            'passport_id',
            'position',
            'sub_position',
            'authorization_letter',
            'media_channel',
            'institution',
            'address',
            'phone_number',
            'phone_number_2',
            'email',
            'birthday',
            'birthplace',
            'blood_type',
            'created_by',
            'type',
            'authorized_by',
        ]


# class NationalAccreditationForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         for visible in self.visible_fields():
#             if visible.field.label != 'Tipo de acreditación':
#                 visible.field.widget.attrs['class'] = 'input input-bordered w-full'

#     # Personal Data
#     first_name = forms.CharField(label='Nombre', max_length=120)
#     last_name = forms.CharField(label='Apellido', max_length=120)
#     institution = forms.CharField(label='Institución/Empresa', max_length=120)
#     position = forms.CharField(label='Cargo en el evento', max_length=120)
#     id_document = forms.CharField(label='Cedula/Pasaporte', max_length=120)
#     address = forms.CharField(label='Dirección', max_length=120)
#     email = forms.EmailField(label='Email', max_length=120)
#     birthday = forms.DateField(label='Fecha de nacimiento',
#                                widget=forms.DateInput(
#                                    format=('%d/%m/%Y'),
#                                    attrs={
#                                        'type': 'date'
#                                    }
#                                 ))
#     birthplace = forms.CharField(label='Lugar de nacimiento')
#     blood_type = forms.CharField(label='Tipo de sangre')

#     type_of_accreditation = forms.CharField(
#         label='Tipo de acreditación',
#         widget=forms.RadioSelect(
#             attrs={'class': 'radio'},
#             choices=[
#                 ('1', 'Coordinación general'),
#                 ('2', 'Protocolo'),
#                 ('3', 'Seguridad'),
#                 ('4', 'Personal Técnico'),
#                 ('5', 'Delegación oficial'),
#                 ('6', 'Enlace (protocolo-enlace)'),
#                 ('7', 'Proveedor'),
#                 ('8', 'Comisión de Prensa'),
#             ]
#         )
#     )
