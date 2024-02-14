from django import forms

from core.models import SecurityWeaponAccreditation

class SecurityWeaponAccreditationForm(forms.ModelForm):
    class Meta:
        model = SecurityWeaponAccreditation
        fields = '__all__'

# class SecurityWeaponsRegistrationForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        
#         for visible in self.visible_fields():
#             if visible.field.label != 'Tipo de acreditación':
#                 visible.field.widget.attrs['class'] = 'input input-bordered w-full'

#     country_of_origin = forms.CharField(
#         label='Pais de origen', 
#         widget=forms.Select(
#             choices=[
#                 ('1', 'Guatemala'),
#                 ('1', 'Costa Rica'),
#                 ('1', 'Nicaragua'),
#                 ('1', 'El Salvador'),
#                 ('1', 'Mexico'),
#                 ('1', 'Estados Unidos'),
#             ]
#         ),
#     )
    
#     name = forms.CharField(label='Nombre')
#     position = forms.CharField(label='Cargo')
#     nationality = forms.CharField(label='Nacionalidad')
#     control_date = forms.DateField(
#         label='Fecha de Control', 
#         widget=forms.DateInput(
#             format=('%d/%m/%Y'),
#             attrs={'type': 'date'}
#         ),
#     )
#     control_time = forms.TimeField(
#         label='Hora de Control', 
#         widget=forms.TimeInput(
#             format=('%H:%M'),
#             attrs={'type': 'time'}
#         ),
#     )
    
#     weapon = forms.CharField(label='Arma')
#     weapon_brand = forms.CharField(label='Marca')
#     weapon_model = forms.CharField(label='Modelo')
#     weapon_type = forms.CharField(label='Tipo')
#     weapon_serial_no = forms.CharField(label='Serie No')
#     weapon_caliber = forms.CharField(label='Calibre')
#     weapon_chargers = forms.CharField(label='Cantidad de Cargadores')
#     weapon_ammunition = forms.CharField(label='Total de Municiones')

#     equipment_radio = forms.CharField(label='Radio')
#     equipment_radio_mode = forms.CharField(label='Modelo de Radio')
#     equipment_radio_type = forms.CharField(label='Tipo de Radio')
#     equipment_radio_series = forms.CharField(label='Serie de Radio')
#     equipment_radio_frequency = forms.CharField(label='Frecuencia de Radio')
    
#     arrival_date = forms.DateField(
#         label='Fecha de Llegada',
#         widget=forms.DateInput(
#             format=('%d/%m/%Y'),
#             attrs={'type': 'date'}
#         ),
#     )
#     arrival_time = forms.TimeField(
#         label='Hora de Llegada',
#         widget=forms.TimeInput(
#             format=('%H:%M'),
#             attrs={'type': 'time'}
#         ),
#     )
#     arrival_flight = forms.CharField(label='Vuelo No de Llegada')
#     arrival_airport = forms.CharField(label='Aeropuerto de Llegada')
    
#     departure_date = forms.DateField(
#         label='Fecha de Salida',
#         widget=forms.DateInput(
#             format=('%d/%m/%Y'),
#             attrs={'type': 'date'}
#         ),
#     )
#     departure_time = forms.TimeField(
#         label='Hora de Salida',
#         widget=forms.TimeInput(
#             format=('%H:%M'),
#             attrs={'type': 'time'}
#         ),
#     )
#     departure_flight = forms.CharField(label='Vuelo No de Salida')
#     departure_airport = forms.CharField(label='Aeropuerto de Salida')
    
#     observations = forms.CharField(label='Observaciones')
