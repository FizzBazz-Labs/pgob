from django.contrib.auth import get_user_model

from rest_framework import serializers


class ChangePasswordSerializer(serializers.Serializer):
    model = get_user_model()

    password = serializers.CharField(required=True)
    password_confirm = serializers.CharField(required=True)

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("The new passwords do not match.")

        return data
