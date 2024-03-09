from rest_framework import serializers
from countries.serializers import CountrySerializer

from vehicle_access_airport_accreditations.models import VehicleAccessAirportAccreditations

from vehicles.serializers import VehicleSerializer

from core.serializers import UserSerializer


class VehicleAccessAirportAccreditationsSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    vehicles = VehicleSerializer(many=True)

    class Meta:
        model = VehicleAccessAirportAccreditations
        fields = [
            'id',
            'country',
            'information_responsible',
            'vehicles',
            'created_by',
            'status',
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

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['country'] = instance.country.name if instance.country else None
        representation['created_by'] = UserSerializer(instance.created_by).data
        return representation


class VehicleAccessAirportAccreditationsReadSerializer(VehicleAccessAirportAccreditationsSerializer):
    vehicles = VehicleSerializer(many=True)
    country = CountrySerializer()
