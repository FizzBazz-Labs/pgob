from rest_framework import serializers

from security_accreditations.models import SecurityWeaponAccreditation

from equipments.serializers import EquipmentSerializer

from security_accreditations.models import Weapon

from core.serializers import UserSerializer


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = [
            'id',
            'weapon',
            'brand',
            'model',
            'type',
            'serial',
            'caliber',
            'chargers',
            'ammunition',
            'created_at',
            'updated_at'
        ]


class SecurityWeaponAccreditationSerializer(serializers.ModelSerializer):
    communication_items = EquipmentSerializer(many=True)
    weapons = WeaponSerializer(many=True)

    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = SecurityWeaponAccreditation
        fields = [
            'id',
            'control_datetime',
            'weapons',
            'communication_items',
            'observations',
            'created_by',
            'created_at',
            'updated_at',
            'status',
            'country',
            'name',
            'passportNo',
            'position',
            'dateArrival',
            'hourArrival',
            'flightNumberArrival',
            'airportArrival',
            'dateDeparture',
            'hourDeparture',
            'flightNumberDeparture',
            'airportDeparture',
        ]

    def create(self, validated_data):
        communication_items_data = validated_data.pop('communication_items')
        weapons_data = validated_data.pop('weapons')
        instance = super().create(validated_data)
        self._update_communication_items(instance, communication_items_data)
        self._update_weapons(instance, weapons_data)
        return instance

    def update(self, instance, validated_data):
        communication_items_data = validated_data.pop(
            'communication_items', [])
        instance = super().update(instance, validated_data)
        self._update_communication_items(instance, communication_items_data)
        self._update_weapons(instance, validated_data.get('weapons', []))
        return instance

    def _update_communication_items(self, instance, communication_items_data):
        existing_communication_item_ids = instance.communication_items.values_list(
            'id', flat=True)

        # Delete communication items not present in the updated data
        for communication_item in instance.communication_items.all():
            if communication_item.id not in [data.get('id') for data in communication_items_data]:
                communication_item.delete()

        # Create or update communication items
        for communication_item_data in communication_items_data:
            communication_item_id = communication_item_data.get('id')
            if communication_item_id in existing_communication_item_ids:
                communication_item = instance.communication_items.get(
                    id=communication_item_id)
                EquipmentSerializer().update(communication_item, communication_item_data)
            else:
                instance.communication_items.create(**communication_item_data)

    def _update_weapons(self, instance, weapons_data):
        existing_weapons_ids = instance.weapons.values_list('id', flat=True)

        # Delete communication items not present in the updated data
        for weapon in instance.weapons.all():
            if weapon.id not in [data.get('id') for data in weapons_data]:
                weapon.delete()

        # Create or update communication items
        for weapon in weapons_data:
            weapon_id = weapon.get('id')
            if weapon_id in existing_weapons_ids:
                weapon_item = instance.weapons.get(id=weapon_id)
                WeaponSerializer().update(weapon_item, weapon)
            else:
                instance.weapons.create(**weapon)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_by'] = UserSerializer(
            instance.created_by).data
        return representation
