from rest_framework.decorators import api_view, authentication_classes
from core.authentication import MyAuthentication
from rest_framework.response import Response
from rest_framework import status
from core.models import User
from utils.helper import log
from ..serializers.feed_post_pic_serializers import FollowingPostPicSerializer


@api_view(http_method_names=['get'])
@authentication_classes([MyAuthentication])
def get_post_pic_list(request):
    current_user: User = request.user
    queryset = current_user.following.all()
    log('DATA', queryset)
    serializer = FollowingPostPicSerializer(queryset, many=True)
    return Response(serializer.data)