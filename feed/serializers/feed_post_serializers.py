from remit.serializers.follow_serializers import GetFollowSerializer
from remit.serializers.post_serializer import PostSerializer
from rest_framework import serializers

class FeedUserPostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    posts = PostSerializer(many=True)

class FeedPostsSerializer(serializers.Serializer):
    follow_user = FeedUserPostSerializer()
    