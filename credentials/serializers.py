from rest_framework.serializers import ModelSerializer

from credentials.models import VehicleCertification


class VehicleCertificationSerializer(ModelSerializer):
    class Meta:
        model = VehicleCertification
        fields = '__all__'
