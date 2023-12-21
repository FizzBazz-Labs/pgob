from django import forms


class NewsletterNationalForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
            if visible.field.label != 'Tipo de acreditación':
                visible.field.widget.attrs['class'] = 'input input-bordered w-full'

    country = forms.CharField(label='País')
    first_name = forms.CharField(label='Nombre', max_length=120)
    last_name = forms.CharField(label='Apellido', max_length=120)
    nationality = forms.CharField(label='Nacionalidad')
    dni = forms.CharField(label='Cédula')
    position = forms.CharField(label='Cargo en el evento', max_length=120)    
    phone_number = forms.CharField(label='Teléfono')
    media_channels = forms.CharField(
        label='Medios de Comunicación',
        widget=forms.Select(
            attrs={'class': 'radio'},
            choices=[
                ('1', 'Prensa'),
                ('2', 'Radio'),
                ('3', 'Internet'),
                ('4', 'Televisión '),
                ('5', 'Agencia Internacional'),
            ]
        )
    )
    media = forms.CharField(label='Medio de Comunicación')
    media_address = forms.CharField(label='Dirección')
    media_phone_number = forms.CharField(label='Teléfono')
    media_fax = forms.CharField(label='Fax')
    media_email = forms.CharField(label='Email')
    media_date = forms.DateField(
        label='Fecha', 
        widget=forms.DateInput(
            format=('%d/%m/%Y'),
            attrs={'type': 'date'}
        ),
    )
