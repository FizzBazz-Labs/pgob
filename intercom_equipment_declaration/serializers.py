from rest_framework import serializers

from intercom_equipment_declaration.models import IntercomEquipmentDeclaration

from countries.serializers import CountrySerializer
from countries.models import Country

from equipments.serializers import EquipmentSerializer

from core.serializers import UserSerializer


class IntercomEquipmentDeclarationSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault())
    equipments = EquipmentSerializer(many=True)

    class Meta:
        model = IntercomEquipmentDeclaration
        fields = [
            'id',
            'country',
            'institution',
            'equipments',
            'created_by',
            'status',
            'created_at',
            'updated_at',
            'reviewed_by',
            'authorized_by',
            'rejected_by',
            'certificated',
            'certification',
            'reviewed_comment',
            'authorized_comment',
            'uuid',
        ]

        read_only_fields = [
            'created_at',
            'updated_at',
            'reviewed_by',
            'authorized_by',
            'rejected_by',
            'certificated',
            'certification',
            'reviewed_comment',
            'authorized_comment',
            'uuid',
        ]

    def create(self, validated_data):
        equipments_data = validated_data.pop('equipments')
        instance = super().create(validated_data)
        self._update_equipments(instance, equipments_data)
        return instance

    def update(self, instance, validated_data):
        equipments_data = validated_data.pop('equipments', [])
        instance = super().update(instance, validated_data)
        self._update_equipments(instance, equipments_data)
        return instance

    def _update_equipments(self, instance, equipments_data):
        existing_equipment_ids = instance.equipments.values_list(
            'id', flat=True)

        # Delete equipments not present in the updated data
        for equipment in instance.equipments.all():
            if equipment.id not in [data.get('id') for data in equipments_data]:
                equipment.delete()

        # Create or update equipments
        for equipment_data in equipments_data:
            equipment_id = equipment_data.get('id')
            if equipment_id in existing_equipment_ids:
                equipment = instance.equipments.get(id=equipment_id)
                EquipmentSerializer().update(equipment, equipment_data)
            else:
                instance.equipments.create(**equipment_data)

    def to_internal_value(self, data):
        data['country'] = self.context['request'].user.profile.country.pk
        return super().to_internal_value(data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['country'] = CountrySerializer(instance.country).data
        representation['created_by'] = UserSerializer(instance.created_by).data

        return representation
