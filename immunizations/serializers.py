from rest_framework import serializers

from immunizations.models import Immunization


class ImmunizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Immunization
        fields = ['id', 'name',]
