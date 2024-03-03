from rest_framework import serializers

from positions.models import Position, SubPosition


class SubPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubPosition
        fields = ['id', 'name']


class PositionSerializer(serializers.ModelSerializer):
    sub_positions = SubPositionSerializer(many=True, read_only=True)

    class Meta:
        model = Position
        fields = ['id', 'name', 'sub_positions']
