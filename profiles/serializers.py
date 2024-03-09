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
    groups = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(), many=True)
    country = serializers.PrimaryKeyRelatedField(
        source='profile.country', queryset=Country.objects.all())

    accreditations = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Accreditation.objects.all())

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
            'groups',
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

    def add_to_group(self, user, group_id):
        group = Group.objects.get(id=group_id)
        user.groups.add(group)

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', {})

        groups = validated_data.pop('groups', [])
        country = profile_data.get('country')
        phone_number = profile_data.get('phone_number')

        user = get_user_model().objects.create(**validated_data)
        user.set_password(user.password)
        user.save()
        user.groups.set(groups)

        self.create_profile(user, phone_number, country)
        return user
