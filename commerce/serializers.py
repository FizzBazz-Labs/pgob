from rest_framework import serializers

from commerce.models import Commerce


class CommerceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commerce
        fields = '__all__'
