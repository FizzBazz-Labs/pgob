from rest_framework import serializers

from intercom_equipment_declaration.models import IntercomEquipmentDeclaration

from countries.serializers import CountrySerializer

from equipments.serializers import EquipmentSerializer

class IntercomEquipmentDeclarationSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    equipments = EquipmentSerializer(many=True)

    class Meta:
        model = IntercomEquipmentDeclaration
        fields = [
            'country',
            'institution',
            'equipments',
            'created_by',
        ]

    def create(self, validated_data):
        equipments = validated_data.pop('equipments')
        intercom_equipment_declaration = IntercomEquipmentDeclaration.objects.create(
            **validated_data)

        for item in equipments:
            intercom_equipment_declaration.equipments.create(**item)

        return intercom_equipment_declaration

class IntercomEquipmentDeclarationReadSerializer(IntercomEquipmentDeclarationSerializer):
    country = CountrySerializer()
    equipments = EquipmentSerializer(many=True)