from django import forms


class OverflightNonCommercialAircraftForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            if visible.field.label != 'Tipo de acreditación':
                visible.field.widget.attrs['class'] = 'input input-bordered w-full'

    country = forms.CharField(label='País')

    # Aircraft Information
    aircraft_type = forms.CharField(label='Tipo')
    aircraft_model = forms.CharField(label='Modelo')
    aircraft_ownership = forms.CharField(
        label='Propiedad',
        widget=forms.Select(
            attrs={'class': 'radio'},
            choices=[
                ('1', 'Civil'),
                ('2', 'Militar'),
            ]
        )
    )
    aircraft_ownership = forms.CharField(
        label='Propiedad',
        widget=forms.Select(
            attrs={'class': 'radio'},
            choices=[
                ('1', 'Civil'),
                ('2', 'Militar'),
            ]
        )
    )
    aircraft_registration = forms.CharField(label='Matrícula')
    aircraft_color = forms.CharField(label='Color')
    aircraft_call_id = forms.CharField(label='Indicativo de Llamada')

    commander_name = forms.CharField(label='Nombre del Comandante')
    crew_members_number = forms.IntegerField(label='No de Tripulantes')
    pmi_name = forms.CharField(label='Nombre del PMI')
    pmi_position = forms.CharField(label='Cargo')
    passengers_number = forms.IntegerField(label='No de Pasajeros')
    
    # Flight Information
    flight_arrival_date = forms.DateField(
        label='Fecha de Entrada a Territario Nacional', 
        widget=forms.DateInput(
            format=('%d/%m/%Y'),
            attrs={'type': 'date'}
        ),
    )
    flight_departure_date = forms.DateField(
        label='Fecha de Salida a Territario Nacional', 
        widget=forms.DateInput(
            format=('%d/%m/%Y'),
            attrs={'type': 'date'}
        ),
    )

    overflight_dates_places = forms.CharField(label='Fecha(s), Lugar (es) y objeto de Sobrevuelo')
    arrival_dates_places = forms.CharField(label='Fechas (s) Lugar (es) y objetivo del aterrizaje')

    overflight_origin = forms.CharField(label='Procedencia')
    overflight_destinity = forms.CharField(label='Destino')
    overflight_journey = forms.CharField(label='Ruta')
    overflight_facelities = forms.CharField(label='Facilidades que la aeronave requiere en tierra')
    
    date = forms.DateField(
        label='Fecha de Salida a Territario Nacional', 
        widget=forms.DateInput(
            format=('%d/%m/%Y'),
            attrs={'type': 'date'}
        ),
    )
    
    applicant_sign = forms.CharField(label='Firma del solicitante')
