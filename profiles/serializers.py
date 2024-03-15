from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.utils.translation import gettext as _

from rest_framework import serializers

from core.serializers import AccreditationSerializer
from core.models import Accreditation

from profiles.models import Profile

from countries.models import Country


class ProfileSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(source='profile.phone_number')
    group = serializers.SerializerMethodField()
    country = serializers.CharField(source='profile.country.name')
    passport_id = serializers.CharField(source='profile.passport_id')
    accreditations = AccreditationSerializer(
        many=True, read_only=True,
        source='profile.accreditations')

    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'group',
            'country',
            'passport_id',
            'accreditations',
        ]

    def get_group(self, obj) -> str:
        return obj.groups.first().name if obj.groups.first() else None


class UserRegisterSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(source='profile.phone_number')
    passport_id = serializers.CharField(source='profile.passport_id')
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    country = serializers.PrimaryKeyRelatedField(
        source='profile.country', queryset=Country.objects.all())

    group = serializers.CharField(write_only=True, required=True)

    accreditations = serializers.ListField(
        child=serializers.CharField(), write_only=True)

    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'passport_id',
            'email',
            'phone_number',
            'password',
            'group',
            'country',
            'accreditations',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'accreditations': {'required': True}
        }

    def validate_email(self, email: str):
        already_user_email = get_user_model().objects\
            .filter(email__exact=email.strip())\
            .exists()

        if already_user_email:
            raise serializers.ValidationError(
                _('A user is already registered with this e-mail address.'))

        return email

    def create_profile(self, user, phone_number, country):
        Profile.objects.create(
            user=user,
            phone_number=phone_number,
            country=country
        )

    def add_to_group(self, user, group_name: str):
        group = Group.objects.get(name=group_name)
        user.groups.add(group)

    def add_accreditations(self, user, accreditations):

        for accreditation in accreditations:
            instance, _ = Accreditation.objects.get_or_create(
                name=accreditation)
            user.profile.accreditations.add(instance)

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', {})
        accreditations = validated_data.pop('accreditations', [])

        group = validated_data.pop('group', '')
        country = profile_data.get('country')
        phone_number = profile_data.get('phone_number')

        user = get_user_model().objects.create(**validated_data)
        user.set_password(user.password)
        user.save()
        self.create_profile(user, phone_number, country)
        self.add_accreditations(user, accreditations)
        self.add_to_group(user, group)
        return user