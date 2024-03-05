from rest_framework import serializers

from international_accreditation.models import InternationalAccreditation
from national_accreditation.models import NationalAccreditation


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()


class AccreditationsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField()
    type = serializers.CharField()
    country = serializers.CharField()
    status = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    created_by = UserSerializer(read_only=True)
