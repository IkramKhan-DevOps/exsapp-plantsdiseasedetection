from rest_framework import serializers
from src.accounts.models import User
from src.api.models import Capture


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


class CaptureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capture
        fields = [
            'image', 'x_axis', 'y_axis', 'is_active'
        ]
