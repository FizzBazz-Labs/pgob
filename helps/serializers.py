from rest_framework import serializers

from helps.models import HelpSection, HelpSectionItem


class HelpSectionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpSectionItem
        fields = '__all__'


class HelpSectionSerializer(serializers.ModelSerializer):
    items = HelpSectionItemSerializer(many=True, read_only=True)

    class Meta:
        model = HelpSection
        fields = '__all__'
