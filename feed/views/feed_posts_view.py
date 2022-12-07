from rest_framework.decorators import api_view, authentication_classes
from core.authentication import MyAuthentication
from rest_framework.response import Response
from rest_framework import status
from remit.models import Post , Following
from ..serializers.feed_post_serializers import FeedPostsSerializer

# Create your views here.
@api_view(http_method_names=['get'])
@authentication_classes([MyAuthentication])
def get_feed_posts(request):
    current_user_id = request.user.id
    follow_queryset = Following.objects.filter(current_user_id=current_user_id)
    serializer = FeedPostsSerializer(follow_queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
