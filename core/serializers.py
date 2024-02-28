from rest_framework import serializers


class AccreditationListSerializer(serializers.Serializer):
    created_at = serializers.CharField()
    country = serializers.CharField()
    type = serializers.CharField()
    authorized_by = serializers.CharField()
    id = serializers.IntegerField()