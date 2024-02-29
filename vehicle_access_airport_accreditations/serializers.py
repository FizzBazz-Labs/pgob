from rest_framework import serializers

from vehicle_access_airport_accreditations.models import VehicleAccessAirportAccreditations

from countries.serializers import CountrySerializer

from vehicles.serializers import VehicleSerializer

class VehicleAccessAirportAccreditationsSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    vehicles = VehicleSerializer(many=True)

    class Meta:
        model  = VehicleAccessAirportAccreditations
        fields = [
            'country',
            'information_responsible',
            'vehicles',
            'created_by',
        ]

    def create(self, validated_data):
        vehicles = validated_data.pop('vehicles')
        vehicle_access_airport_acreditations = VehicleAccessAirportAccreditations.objects.create(
            **validated_data)

        for item in vehicles:
            vehicle_access_airport_acreditations.vehicles.create(**item)

        return vehicle_access_airport_acreditations


class VehicleAccessAirportAccreditationsReadSerializer(VehicleAccessAirportAccreditationsSerializer):
    country = CountrySerializer()
    vehicles = VehicleSerializer(many=True)