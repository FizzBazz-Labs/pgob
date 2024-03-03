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
           'mission',
           'assigned_by',
           'vehicles',
           'distinctive',
           'observations',
           'created_by'
      ]

    def create(self, validated_data):
        vehicles = validated_data.pop('vehicles')
        general_vehicle_acreditation = GeneralVehicleAccreditation.objects.create(
            **validated_data)

        for item in vehicles:
            general_vehicle_acreditation.vehicles.create(**item)

        return general_vehicle_acreditation
    
class GeneralVehicleAccreditationReadSerializer(GeneralVehicleAccreditationSerializer):
    vehicles = VehicleSerializer(many=True)