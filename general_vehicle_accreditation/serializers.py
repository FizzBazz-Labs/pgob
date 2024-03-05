from rest_framework import serializers
from general_vehicle_accreditation.models import GeneralVehicleAccreditation
from vehicles.serializers import VehicleSerializer


class GeneralVehicleAccreditationSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    vehicles = VehicleSerializer(many=True)

    class Meta:
        model = GeneralVehicleAccreditation
        fields = [
            'pk',
            'mission',
            'assigned_to',
            'vehicles',
            'distinctive',
            'observations',
            'created_by'
        ]

    def create(self, validated_data):
        vehicles_data = validated_data.pop('vehicles')
        instance = super().create(validated_data)
        self._update_vehicles(instance, vehicles_data)
        return instance

    def update(self, instance, validated_data):
        vehicles_data = validated_data.pop('vehicles', [])
        instance = super().update(instance, validated_data)
        self._update_vehicles(instance, vehicles_data)
        return instance

    def _update_vehicles(self, instance, vehicles_data):
        existing_vehicle_ids = instance.vehicles.values_list('id', flat=True)

        # Delete vehicles not present in the updated data
        for vehicle in instance.vehicles.all():
            if vehicle.id not in [data.get('id') for data in vehicles_data]:
                vehicle.delete()

        # Create or update vehicles
        for vehicle_data in vehicles_data:
            vehicle_id = vehicle_data.get('id')
            if vehicle_id in existing_vehicle_ids:
                vehicle = instance.vehicles.get(id=vehicle_id)
                VehicleSerializer().update(vehicle, vehicle_data)
            else:
                instance.vehicles.create(**vehicle_data)
