from django import forms

from core.models import VehicleAccessAirport


class VehicleAccessAirportForm(forms.ModelForm):
    class Meta:
        model = VehicleAccessAirport
        fields = '__all__'


# class VehicleAccessAirportForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'input input-bordered w-full'

#     country = forms.CharField(
#         label='Nombre del pais',
#         widget=forms.Select(
#             attrs={'class': 'radio'},
#             choices=[
#                 ('1', 'Guatemala'),
#                 ('1', 'Costa Rica'),
#                 ('1', 'Nicaragua'),
#                 ('1', 'El Salvador'),
#                 ('1', 'Mexico'),
#                 ('1', 'Estados Unidos'),
#             ]
#         ))
    
#     vehicle_type = forms.CharField(label='Tipo', max_length=120)
#     vehicle_brand= forms.CharField(label='Marca/Modelo', max_length=120)
#     vehicle_color = forms.CharField(label='Color', max_length=120)
#     vehicle_plate = forms.CharField(label='Placa No.', max_length=120)
#     vehicle_driver = forms.CharField(label='Conductor', max_length=120)
#     vehicle_driver_id = forms.CharField(label='Cedula', max_length=120)
#     responsible_for_the_information = forms.CharField(
#         label='Responsable de la información',
#         max_length=120,
#     )
