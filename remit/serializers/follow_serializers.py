from rest_framework import serializers
from core.serializers import UserSerializer

class CreateFollowSerializer(serializers.Serializer):
    username = serializers.CharField()

class FollowSerializer(serializers.Serializer):
    current_user = serializers.PrimaryKeyRelatedField(read_only=True)
    follow_user = serializers.PrimaryKeyRelatedField(read_only=True)

class GetFollowSerializer(serializers.Serializer):
    follow_user = UserSerializer()