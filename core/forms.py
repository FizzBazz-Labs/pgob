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
    
