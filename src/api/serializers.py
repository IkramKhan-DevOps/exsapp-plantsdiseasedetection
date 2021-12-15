from rest_framework import serializers
from src.accounts.models import User
from src.api.models import Capture, Plant, PlantImage, Disease, DiseaseImage, Canopy


class UserPasswordChangeSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'pk', 'profile_image', 'first_name', 'last_name', 'username',
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'pk', 'profile_image', 'first_name', 'last_name', 'username', 'email', 'phone_number'
        ]
        read_only_fields = [
            'email', 'date_joined'
        ]


""" CAPTURES """


class CanopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Canopy
        fields = '__all__'


class CaptureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capture
        fields = [
            'image', 'x_axis', 'y_axis', 'is_active'
        ]


class PlantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantImage
        fields = '__all__'


class PlantSerializer(serializers.ModelSerializer):
    canopy = CanopySerializer(many=False, read_only=True)
    images = PlantImageSerializer(many=True, read_only=True)

    class Meta:
        model = Plant
        fields = [
            'name', 'description', 'canopy', 'is_active', 'created_on', 'updated_on', 'images'
        ]


class DiseaseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseImage
        fields = '__all__'


class DiseaseSerializer(serializers.ModelSerializer):
    images = DiseaseImageSerializer(many=True, read_only=True)

    class Meta:
        model = Disease
        fields = [
            'name', 'description', 'is_active', 'created_on', 'updated_on', 'images'
        ]
