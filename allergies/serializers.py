from rest_framework import serializers

from allergies.models import Allergy


class AllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergy
        fields = ['id', 'name']
