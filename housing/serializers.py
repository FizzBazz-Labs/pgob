from rest_framework import serializers

from housing.models import Housing


class HousingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Housing
        fields = '__all__'
