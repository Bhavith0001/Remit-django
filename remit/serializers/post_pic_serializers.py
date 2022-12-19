from rest_framework import serializers

class CurrentUserPostPicSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    caption = serializers.CharField()
    post_image = serializers.ImageField()
    total_likes = serializers.SerializerMethodField()

    def get_total_likes(self, instance):
        return instance.likes.count()