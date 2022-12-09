from remit.serializers.post_serializer import PostSerializer
from rest_framework import serializers

class FeedUserPostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    posts = PostSerializer(many=True)
    