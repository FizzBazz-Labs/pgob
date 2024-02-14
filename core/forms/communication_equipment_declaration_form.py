from django import forms

from core.models import CommunicationEquipmentDeclaration



class CommunicationEquipmentDeclarationForm(forms.ModelForm):
    class Meta:
        model = CommunicationEquipmentDeclaration
        fields = '__all__'