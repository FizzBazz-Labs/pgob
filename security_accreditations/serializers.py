from rest_framework import serializers
from security_accreditations.models import SecurityWeaponAccreditation
from equipments.serializers import EquipmentSerializer


class SecurityWeaponAccreditationSerializer(serializers.ModelSerializer):
    communication_items = EquipmentSerializer(many=True)
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

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
        communication_items_data = validated_data.pop('communication_items')
        instance = super().create(validated_data)
        self._update_communication_items(instance, communication_items_data)
        return instance

    def update(self, instance, validated_data):
        communication_items_data = validated_data.pop('communication_items', [])
        instance = super().update(instance, validated_data)
        self._update_communication_items(instance, communication_items_data)
        return instance

    def _update_communication_items(self, instance, communication_items_data):
        existing_communication_item_ids = instance.communication_items.values_list('id', flat=True)

        # Delete communication items not present in the updated data
        for communication_item in instance.communication_items.all():
            if communication_item.id not in [data.get('id') for data in communication_items_data]:
                communication_item.delete()

        # Create or update communication items
        for communication_item_data in communication_items_data:
            communication_item_id = communication_item_data.get('id')
            if communication_item_id in existing_communication_item_ids:
                communication_item = instance.communication_items.get(id=communication_item_id)
                EquipmentSerializer().update(communication_item, communication_item_data)
            else:
                instance.communication_items.create(**communication_item_data)
