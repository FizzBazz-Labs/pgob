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


class NationalSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    allergies = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Allergy.objects.all())
    immunizations = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Immunization.objects.all())
    medicals = serializers.PrimaryKeyRelatedField(
        many=True, queryset=MedicalHistory.objects.all())

    class Meta:
        model = NationalAccreditation
        fields = [
            'id',
            'image',
            'first_name',
            'last_name',
            'position',
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
            'downloaded',
            'uuid',
            'reviewed_comment',
        ]

        extra_kwargs = {
            'downloaded': {'read_only': True},
            'uuid': {'read_only': True},
        }

        def create(self, validated_data):
            allergies = validated_data.pop('allergies', [])
            immunizations = validated_data.pop('immunizations', [])
            medicals = validated_data.pop('medicals', [])

            instance = super().create(validated_data)

            instance.allergies.set(allergies)
            instance.immunizations.set(immunizations)
            instance.medicals.set(medicals)

            return instance


class NationalUpdateSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = NationalAccreditation
        fields = [
            'id',
            'image',
            'first_name',
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
