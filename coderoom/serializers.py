from rest_framework import serializers
from .models import CodeRoom
from accounts.serializer import UserSerializer


class CodeRoomSerializer(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = CodeRoom
        fields = "__all__"
        read_only_fields = ["owner"]


class CodeRoomSerializerForCreate(serializers.ModelSerializer):
    class Meta:
        model = CodeRoom
        fields = "__all__"
