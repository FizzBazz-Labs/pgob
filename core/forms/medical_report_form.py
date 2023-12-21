from django import forms


class MedicalReportForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        labels = ['Tipo de alergias', 'Inmunizaciones Recientes', 'Antecedentos Medicos']
        
        for visible in self.visible_fields():
            if visible.field.label not in labels:
                visible.field.widget.attrs['class'] = 'input input-bordered w-full'
            
    # Personal Data
    country = forms.CharField(label='Nombre del pais', max_length=120)
    authority_name = forms.CharField(label='Nombre de la autoridad', max_length=120)
    position = forms.CharField(label='Cargo', max_length=120)
    age = forms.IntegerField(
        label='Edad', 
        widget=forms.NumberInput(
            attrs={
            'type': 'number'
            }
        )
    )
    blood_type = forms.CharField(label='Tipo de sangre')
    
    factor_rh = forms.CharField(label='Factor RH', max_length=120)
    diseases_under_treatment = forms.CharField(
        label='Lugar de nacimiento',
        widget=forms.Textarea()
    )

    medication_in_use = forms.CharField(label='Medicamentos en uso', max_length=120)
    surgical_history = forms.CharField(label='Antecedentes Quirurgicos')
    doctor_name = forms.CharField(label='Nombre del medico', max_length=120)
    doctor_residential = forms.CharField(label='Lugar de hospedaje en Panama', max_length=120)
    doctor_phone = forms.CharField(label='Telefono', max_length=120)
    doctor_relevant_information = forms.CharField(label='Información Relevante', max_length=120)

    responsible_for_the_information = forms.CharField(label='Responsable de la informacion', max_length=120)

    allergies = forms.CharField(
        label='Tipo de alergias',
        widget=forms.RadioSelect(
            attrs={'class': 'radio'},
            choices=[
                ('1', 'Ambientales'),
                ('2', 'Alimentacias'),
                ('3', 'Analgesicos'),
                ('4', 'Antiobioticos')
            ]
        )
    )

    immunizations = forms.CharField(
        label='Inmunizaciones Recientes',
        widget=forms.RadioSelect(
            attrs={'class': 'radio'},
            choices=[
                ('1', 'Medios de contraste'),
                ('2', 'Tetano'),
                ('3', 'Hepatitis'),
                ('4', 'Otros')
            ]
        )
    )

    medical_history = forms.CharField(
        label='Antecedentos Medicos',
        widget=forms.RadioSelect(
            attrs={'class': 'radio'},
            choices=[
                ('1', 'Cardiopatia Isquemica'),
                ('2', 'Diabetes Mellitus'),
                ('3', 'Hipertension Arterial'),
                ('4', 'Infarto del miocardio'),
                ('4', 'Angina'),
                ('4', 'Marcapaso Definivo'),
                ('4', 'Arritmias'),
                ('4', 'Otros'),
            ]
        )
    )
    