from remit.serializers.post_pic_serializers import CurrentUserPostPicSerializer
from rest_framework import serializers


class FollowingPostPicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    post_picture = CurrentUserPostPicSerializer(many=True)