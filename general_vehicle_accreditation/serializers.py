from django.contrib.auth import get_user_model

from rest_framework import serializers

from general_vehicle_accreditation.models import GeneralVehicleAccreditation

from vehicles.serializers import VehicleSerializer

from countries.models import Country

from core.serializers import UserSerializer


class GeneralVehicleAccreditationSerializer(serializers.ModelSerializer):
    # accreditation_type = serializers.CharField()
    created_by = serializers.PrimaryKeyRelatedField(
        required=False, read_only=True)

    country = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(), default=Country.objects.get(name='Panamá').pk)

    fullname = serializers.SerializerMethodField()

    class Meta:
        model = GeneralVehicleAccreditation
        fields = [
            'accreditation_type',
            'id',
            'country',
            'assigned_to',
            'vehicles',
            'fullname',
            'distinctive',
            'observations',
            'created_by',
            'status',
        ]

    def to_internal_value(self, data):
        internal_values = super().to_internal_value(data)

        if 'created_by' not in data and 'request' in self.context:
            internal_values['created_by'] = self.context['request'].user

        return internal_values

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_by'] = UserSerializer(instance.created_by).data
        # representation['accreditation_type'] = instance.get_accreditation_type_display()

        return representation

    def get_fullname(self, obj):
        return f'{obj.created_by.first_name} {obj.created_by.last_name}'


class GeneralVehicleAccreditationReadSerializer(GeneralVehicleAccreditationSerializer):
    vehicles = VehicleSerializer(many=True, read_only=True)

    # def create(self, validated_data):
    #     vehicles_data = validated_data.pop('vehicles')
    #     instance = super().create(validated_data)
    #     self._update_vehicles(instance, vehicles_data)
    #     return instance

    # def update(self, instance, validated_data):
    #     vehicles_data = validated_data.pop('vehicles', [])
    #     instance = super().update(instance, validated_data)
    #     self._update_vehicles(instance, vehicles_data)
    #     return instance

    # def _update_vehicles(self, instance, vehicles_data):
    #     existing_vehicle_ids = instance.vehicles.values_list('id', flat=True)

    #     # Delete vehicles not present in the updated data
    #     for vehicle in instance.vehicles.all():
    #         if vehicle.id not in [data.get('id') for data in vehicles_data]:
    #             vehicle.delete()

    #     # Create or update vehicles
    #     for vehicle_data in vehicles_data:
    #         vehicle_id = vehicle_data.get('id')
    #         if vehicle_id in existing_vehicle_ids:
    #             vehicle = instance.vehicles.get(id=vehicle_id)
    #             VehicleSerializer().update(vehicle, vehicle_data)
    #         else:
    #             instance.vehicles.create(**vehicle_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_by'] = UserSerializer(instance.created_by).data

        return representation
