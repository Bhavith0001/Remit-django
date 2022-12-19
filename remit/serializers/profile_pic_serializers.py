from rest_framework import serializers

class ProfilePicSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    image = serializers.ImageField()