from django import forms

CHOICES = (
    (0, 'a'),
    (1, 'b'),
    (2, 'c'),
)

class NationalAccreditationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
            if visible.field.label != 'Tipo de acreditación':
                visible.field.widget.attrs['class'] = 'input input-bordered w-full'
            
    # Personal Data
    first_name = forms.CharField(label='Nombre', max_length=120)
    last_name = forms.CharField(label='Apellido', max_length=120)
    institution = forms.CharField(label='Institución/Empresa', max_length=120)
    position = forms.CharField(label='Cargo en el evento', max_length=120)
    id_document = forms.CharField(label='Cedula/Pasaporte', max_length=120)
    address = forms.CharField(label='Dirección', max_length=120)
    email = forms.EmailField(label='Email', max_length=120)
    birthday = forms.DateField(label='Fecha de nacimiento', 
                               widget=forms.DateInput(
                                   format=('%d/%m/%Y'),
                                   attrs={
                                       'type': 'date'
                                   }
                                ))
    birthplace = forms.CharField(label='Lugar de nacimiento')
    blood_type = forms.CharField(label='Tipo de sangre')
    
    type_of_accreditation = forms.CharField(
        label='Tipo de acreditación',
        widget=forms.RadioSelect(
            attrs={'class': 'radio'},
            choices=[
                ('1', 'Coordinación general'),
                ('2', 'Protocolo'),
                ('3', 'Seguridad'),
                ('4', 'Personal Técnico'),
                ('5', 'Delegación oficial'),
                ('6', 'Enlace (protocolo-enlace)'),
                ('7', 'Proveedor'),
                ('8', 'Comisión de Prensa'),
            ]
        )
    )
    

class InternationalAccreditationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
            if visible.field.label != 'Tipo de acreditación':
                visible.field.widget.attrs['class'] = 'input input-bordered w-full'
        
    country_of_origin = forms.CharField(
        label='Pais de origen', 
        widget=forms.Select(
            choices=[
                ('1', 'Guatemala'),
                ('1', 'Costa Rica'),
                ('1', 'Nicaragua'),
                ('1', 'El Salvador'),
                ('1', 'Mexico'),
                ('1', 'Estados Unidos'),
            ]
    ))
    
    # Personal Data
    first_name = forms.CharField(label='Nombre', max_length=120)
    last_name = forms.CharField(label='Apellido', max_length=120)
    institution = forms.CharField(label='Institución/Empresa', max_length=120)
    position = forms.CharField(label='Cargo en el evento', max_length=120)
    id_document = forms.CharField(label='Cedula/Pasaporte', max_length=120)
    address = forms.CharField(label='Dirección', max_length=120)
    email = forms.EmailField(label='Email', max_length=120)
    birthday = forms.DateField(label='Fecha de nacimiento', 
                               widget=forms.DateInput(
                                   format=('%d/%m/%Y'),
                                   attrs={
                                       'type': 'date'
                                   }
                                ))
    birthplace = forms.CharField(label='Lugar de nacimiento')
    blood_type = forms.CharField(label='Tipo de sangre')
    
    # Accommodation place
    hotel = forms.CharField(label='Hotel', max_length=120)
    room_number = forms.CharField(label='Número de habitación', max_length=120)
    planned_address = forms.CharField(label='Dirección prevista en Panamá', max_length=120)
    phone = forms.CharField(label='Teléfono', max_length=120)
    
    type_of_accreditation = forms.CharField(
        label='Tipo de acreditación',
        widget=forms.RadioSelect(
            attrs={'class': 'radio'},
            choices=[
                ('1', 'Jefe de Delegacion Oficial'),
                ('2', 'Delegación oficial'),
                ('3', 'Protocolo'),
                ('4', 'Seguridad'),
                ('5', 'Personal de Apoyo'),
                ('6', 'Prensa Oficial'),
                ('7', 'Tripulacion')
            ]
        )
    )
    
    # Arrived Data
    arrival_date = forms.DateField(
        label='Fecha de llegada a Panama', 
        widget=forms.DateInput(
            format=('%d/%m/%Y'),
            attrs={'type': 'date'},
        ),
    )

    origin = forms.CharField(label='Procedencia', max_length=120)
    flight = forms.CharField(label='Vuelo', max_length=120)
    arrival_time = forms.TimeField(label='Hora de arribo',
                                   widget=forms.TimeInput(
                                       format=('%H:%M'),
                                       attrs={'type': 'time'}
                                   ))
    
    departure_date = forms.DateField(
        label='Fecha de salida de Panama', 
        widget=forms.DateInput(
            format=('%d/%m/%Y'),
            attrs={'type': 'date'}
        ),
    )

    destination = forms.CharField(
        label='Destino',
        widget=forms.Select(
            attrs={'class': 'radio'},
            choices=[
                ('1', 'Guatemala'),
                ('1', 'Costa Rica'),
                ('1', 'Nicaragua'),
                ('1', 'El Salvador'),
                ('1', 'Mexico'),
                ('1', 'Estados Unidos'),
            ]
        )
    )

    departure_flight = forms.CharField(
        label='Vuelo de salida',
        max_length=120,
    )

    departure_time = forms.TimeField(
        label='Hora de partida',
        widget=forms.TimeInput(
            format=('%H:%M'),
            attrs={'type': 'time'}
        ),
    )

class VehicleAccessToTheAirport(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input input-bordered w-full'

    country = forms.CharField(
        label='Nombre del pais',
        widget=forms.Select(
            attrs={'class': 'radio'},
            choices=[
                ('1', 'Guatemala'),
                ('1', 'Costa Rica'),
                ('1', 'Nicaragua'),
                ('1', 'El Salvador'),
                ('1', 'Mexico'),
                ('1', 'Estados Unidos'),
            ]
        ))
    
    vehicle_type = forms.CharField(label='Tipo', max_length=120)
    vehicle_brand= forms.CharField(label='Marca/Modelo', max_length=120)
    vehicle_color = forms.CharField(label='Color', max_length=120)
    vehicle_plate = forms.CharField(label='Placa No.', max_length=120)
    vehicle_driver = forms.CharField(label='Conductor', max_length=120)
    vehicle_driver_id = forms.CharField(label='Cedula', max_length=120)
    responsible_for_the_information = forms.CharField(label='Responsable de la información', max_length=120)


class OverflightAndNonCommercialAircraft(forms.Form):
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
