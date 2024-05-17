from rest_framework import serializers
from countries.serializers import CountrySerializer

from vehicle_access_airport_accreditations.models import VehicleAccessAirportAccreditations

from vehicles.serializers import VehicleSerializer

from core.serializers import UserSerializer


class VehicleAccessAirportAccreditationsSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    # vehicles = VehicleSerializer(many=True)

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

    def to_internal_value(self, data):
        data['country'] = self.context['request'].user.profile.country.pk
        return super().to_internal_value(data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_by'] = UserSerializer(instance.created_by).data
        return representation


class VehicleAccessAirportAccreditationsReadSerializer(VehicleAccessAirportAccreditationsSerializer):
    vehicles = VehicleSerializer(many=True)
    country = CountrySerializer()
