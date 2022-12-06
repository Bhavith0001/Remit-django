from rest_framework import serializers
from core.serializers import UserSerializer

class CreateFriendSerializer(serializers.Serializer):
    username = serializers.CharField()

class FriendSerializer(serializers.Serializer):
    user1 = serializers.PrimaryKeyRelatedField(read_only=True)
    user2 = serializers.PrimaryKeyRelatedField(read_only=True)
    rel_id = serializers.IntegerField()

class GetFriendSerializer(serializers.Serializer):
    user2 = UserSerializer()
    rel_id = serializers.IntegerField()