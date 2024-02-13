from django import form

from core.models import CommunicationEquipmentDeclaration



class CommunicationEquipmentDeclarationForm(forms.ModelForm):
    class Meta:
        model = CommunicationEquipmentDeclaration