from rest_framework.decorators import api_view, authentication_classes
from rest_framework import status
from rest_framework.response import Response
from core.models import User
from core.authentication import MyAuthentication
from core.serializers import UserSerializer
from utils.helper import log
from utils.exceptions import ResponseException
from core.serializers import UserSerializer

@api_view(http_method_names=['get', 'post'])
@authentication_classes([MyAuthentication])
def following(request):
    try:
        current_user: User = request.user
        log('CURRENT USER', current_user.username)

        if request.method == 'GET':
            queryset = current_user.following.all()
            serializer = UserSerializer(queryset, many=True)
            log('DATA', serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if request.method == 'POST':
            log('FOLLOWING USER', current_user.username)
            follow_user_id = User.objects.get(username=request.data['username']).id
            current_user.following.add(follow_user_id)
            return Response({'follow_status': 'followed successfully'}, status=status.HTTP_201_CREATED)
    
    except Exception as e:
        return ResponseException(msg=e)


@api_view(http_method_names=['get', 'delete'])
@authentication_classes([MyAuthentication])
def get_following_user(request, user_id):
    try:
        current_user: User = request.user
        user_following = current_user.following
        if request.method == 'GET':
            log('CURRENT USER', current_user.username)
            user = user_following.get(id=user_id)
            log('FOLLOWING USER', user)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if request.method == 'DELETE':
            log('FOLLOWING USER', current_user.username)
            user_following.remove(user_id)
            return Response({'follow_status': 'unfollowed successfully'}, status=status.HTTP_202_ACCEPTED)

    except Exception as e:
        return ResponseException(msg=e)