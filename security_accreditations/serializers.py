from rest_framework import serializers

from security_accreditations.models import SecurityWeaponAccreditation

from equipments.serializers import EquipmentSerializer
from equipments.models import Equipment


class SecurityWeaponAccreditationSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    communication_items = EquipmentSerializer(many=True)

    class Meta:
        model = SecurityWeaponAccreditation
        fields = [
            'id',
            'control_date',
            'control_time',
            'weapon',
            'brand',
            'model',
            'type',
            'serial',
            'caliber',
            'chargers',
            'ammunition',
            'communication_items',
            'observations',
            'created_by',
            'created_at',
            'updated_at'
        ]

    def create(self, validated_data):
        communication_items = validated_data.pop('communication_items')
        security_accreditation = SecurityWeaponAccreditation.objects.create(
            **validated_data)

        for item in communication_items:
            security_accreditation.communication_items.create(**item)

        return security_accreditation


class SecurityWeaponAccreditationReadSerializer(SecurityWeaponAccreditationSerializer):
    communication_items = serializers.StringRelatedField(many=True)
    created_by = serializers.StringRelatedField()
