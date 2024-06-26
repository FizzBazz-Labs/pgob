from rest_framework import serializers

from allergies.models import Allergy
from allergies.serializers import AllergySerializer
from immunizations.models import Immunization
from immunizations.serializers import ImmunizationSerializer
from media_channels.serializers import MediaChannelSerializer
from medical_histories.models import MedicalHistory
from medical_histories.serializers import MedicalHistorySerializer
from national_accreditation.models import NationalAccreditation
from positions.serializers import PositionSerializer, SubPositionSerializer

from core.serializers import UserSerializer


class NationalSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    allergies = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Allergy.objects.all())
    immunizations = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Immunization.objects.all())
    medicals = serializers.PrimaryKeyRelatedField(
        many=True, queryset=MedicalHistory.objects.all())

    def validate(self, data):
        if self.context['request'].method == 'POST':
            passport_id = data.get('passport_id')
            first_name = data.get('first_name')
            last_name = data.get('last_name')

            if NationalAccreditation.objects.filter(passport_id=passport_id, first_name=first_name,
                                                    last_name=last_name).exists():
                raise serializers.ValidationError(
                    {'error': 'There is already an accreditation with this passport id, first name or last name.'})

        return data

    class Meta:
        model = NationalAccreditation
        fields = [
            'id',
            'image',
            'country',
            'first_name',
            'last_name',
            'position',
            'authorized_comment',
            'private_insurance',
            'sub_position',
            'media_channel',
            'authorization_letter',
            'institution',
            'security_weapon_accreditation',
            'address',
            'phone_number',
            'phone_number_2',
            'email',
            'birthday',
            'birthplace',
            'times_edited',

            # Medical Information
            'blood_type',
            'diseases',
            'medication_1',
            'medication_2',
            'medication_3',
            'medication_4',
            'allergies',
            'allergies_description',
            'immunizations',
            'medicals',
            'surgical',
            'doctor_name',

            'type',
            'status',
            'passport_id',
            'created_by',
            'certificated',
            'certification',
            'uuid',
            'reviewed_comment',
            'passport_id_image',
        ]

        extra_kwargs = {
            'certificated': {'read_only': True},
            'uuid': {'read_only': True},
            'certification': {'read_only': True},
        }

    def to_internal_value(self, data):
        data['country'] = self.context['request'].user.profile.country.pk
        return super().to_internal_value(data)

    def create(self, validated_data):
        allergies = validated_data.pop('allergies', [])
        immunizations = validated_data.pop('immunizations', [])
        medicals = validated_data.pop('medicals', [])

        instance = super().create(validated_data)

        instance.allergies.set(allergies)
        instance.immunizations.set(immunizations)
        instance.medicals.set(medicals)

        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['created_by'] = UserSerializer(instance.created_by).data
        representation['position'] = PositionSerializer(instance.position).data
        if instance.sub_position:
            representation['sub_position'] = SubPositionSerializer(
                instance.sub_position).data

        if instance.media_channel:
            representation['media_channel'] = MediaChannelSerializer(
                instance.media_channel).data
        return representation


class NationalUpdateSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = NationalAccreditation
        fields = [
            'id',
            'image',
            'first_name',
            # 'country',
            'last_name',
            'position',
            'sub_position',
            'media_channel',
            'authorization_letter',
            'private_insurance',
            'institution',
            'address',
            'phone_number',
            'phone_number_2',
            'email',
            'birthday',
            'birthplace',
            'type',
            'status',
            'created_by',
            'security_weapon_accreditation',

            # Medical Information
            'blood_type',
            'diseases',
            'medication_1',
            'medication_2',
            'medication_3',
            'medication_4',
            'allergies',
            'allergies_description',
            'immunizations',
            'medicals',
            'surgical',
            'doctor_name',
        ]

        # Make image and authorization_letter optional
        extra_kwargs = {
            'image': {'required': False},
            'authorization_letter': {'required': False},
        }

    def update(self, instance, validated_data):
        self.update_many_to_many(instance, 'allergies', validated_data)
        self.update_many_to_many(instance, 'immunizations', validated_data)
        self.update_many_to_many(instance, 'medicals', validated_data)

        # Update other fields
        for field, value in validated_data.items():
            setattr(instance, field, value)

        if instance.times_edited == 0:
            print(self.context['request'].user)
            print('times_edited', instance.times_edited)

        instance.save()
        return instance

    def update_many_to_many(self, instance, field_name, validated_data):
        field_data = validated_data.pop(field_name, None)

        if field_data is not None:
            getattr(instance, field_name).set(field_data)
        elif field_name in validated_data:
            getattr(instance, field_name).clear()


class NationalReadSerializer(NationalSerializer):
    position = PositionSerializer()
    sub_position = SubPositionSerializer()
    media_channel = MediaChannelSerializer()
    allergies = AllergySerializer(many=True)
    immunizations = ImmunizationSerializer(many=True)
    medicals = MedicalHistorySerializer(many=True)
