from django.conf import settings
from rest_framework import serializers 
from .models import Room, Message 

User = settings.AUTH_USER_MODEL

class RoomSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = Room
        fields = ("uid", "name", "participants", "created_at")

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Message
        fields = (
            "uid",
            "room",
            "sender",
            "content",
            "is_read",
            "created_at",
        )
        read_only_fields = ("sender",)
