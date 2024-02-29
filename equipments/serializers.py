from rest_framework import serializers

from .models import Equipment


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = [
            'id',
            'brand',
            'model',
            'type',
            'serial',
            'frequency',
            'created_at',
            'updated_at'
        ]
