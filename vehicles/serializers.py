from rest_framework import serializers

from vehicles.models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields=[
            'id',
            'type',
            'brand',
            'color',
            'plate',
            'driver_name',
            'driver_id',
            "phone",
        ]