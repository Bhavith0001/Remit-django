from rest_framework.decorators import api_view, authentication_classes
from core.authentication import MyAuthentication
from rest_framework.response import Response
from rest_framework import status
from core.models import User
from ..serializers.feed_post_serializers import FeedUserPostSerializer
from utils.helper import log

# Create your views here.
@api_view(http_method_names=['get'])
@authentication_classes([MyAuthentication])
def get_feed_posts(request):
    current_user: User = request.user
    log('CURRENT USER', current_user)
    following = current_user.following.all()
    serializer = FeedUserPostSerializer(following, many=True)
    log('CURRENT USER', serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)
