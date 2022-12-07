from rest_framework import serializers

class AddPostSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    title = serializers.CharField()
    body =serializers.CharField()


class PostSerializer(serializers.Serializer):
    title = serializers.CharField()
    body =serializers.CharField()
    posted_at = serializers.DateTimeField()