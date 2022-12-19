from rest_framework.decorators import api_view, authentication_classes
from rest_framework import status
from rest_framework.response import Response
from core.models import User
from core.authentication import MyAuthentication
from core.serializers import UserSerializer
from utils.helper import log
from utils.exceptions import ResponseException
from core.serializers import UserSerializer


@api_view(http_method_names=['get'])
@authentication_classes([MyAuthentication])
def following(request):
    """ gets all the users that are followed by the current user """

    try:
        current_user: User = request.user
        log('CURRENT USER', current_user.username)

        if request.method == 'GET':
            queryset = current_user.following.all()
            serializer = UserSerializer(queryset, many=True)
            log('DATA', serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Exception as e:
        return ResponseException(msg=e)


@api_view(http_method_names=['post'])
@authentication_classes([MyAuthentication])
def get_user(request):
    """ get the user details by taking 'username' as input """

    try:
        data = request.data
        user = User.objects.get(username=data['username'])
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
    except Exception as e:
        return ResponseException(msg=e)


@api_view(http_method_names=['delete', 'post'])
@authentication_classes([MyAuthentication])
def follow_or_unfollow(request, user_id):
    """ follow or unfollow the user using their 'user_id' """
    try:
        current_user: User = request.user
        user_following = current_user.following

        if request.method == 'POST':
            current_user.following.add(user_id)
            return Response({'follow_status': 'followed successfully'}, status=status.HTTP_201_CREATED)

        if request.method == 'DELETE':
            log('FOLLOWING USER', current_user.username)
            user_following.remove(user_id)
            return Response({'follow_status': 'unfollowed successfully'}, status=status.HTTP_202_ACCEPTED)

    except Exception as e:
        return ResponseException(msg=e)