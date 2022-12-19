from rest_framework import serializers


class AddPostSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    title = serializers.CharField()
    body =serializers.CharField()


class PostSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    title = serializers.CharField()
    body =serializers.CharField()
    posted_at = serializers.DateTimeField()
    total_likes = serializers.SerializerMethodField()

    def get_total_likes(self, instance):
        return instance.likes.count()