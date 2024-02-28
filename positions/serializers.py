from rest_framework import serializers

from positions.models import Position, SubPosition


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'name']


class SubPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubPosition
        fields = ['id', 'name']
