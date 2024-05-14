from .models import UserProfile
from rest_framework import serializers
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(source="profile")

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "user_profile",
        ]


class CompleteUserSerializer(serializers.ModelSerializer):
    baseuser = UserSerializer()
    user_profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ("baseuser", "user_profile")
