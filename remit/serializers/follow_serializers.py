from rest_framework import serializers
from core.serializers import UserSerializer

class GetFollowUserSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    username = serializers.CharField()