from rest_framework.decorators import api_view, authentication_classes
from rest_framework import status
from rest_framework.response import Response
from core.models import User
from core.authentication import MyAuthentication
from ..models import Following
from ..serializers.friend_serializer import CreateFriendSerializer, FriendSerializer, GetFriendSerializer
import structlog
from utils.helper import log
from utils.exceptions import ResponseException


@api_view(http_method_names=['get', 'post'])
@authentication_classes([MyAuthentication])
def following(request):
    try:
        current_user_id = int(request.user.id)

        print('\n\n')
        log('CURRENT USER', current_user_id)

        if request.method == 'GET':
            log('REQUEST', request.method)

            queryset = Following.objects.filter(user1_id=current_user_id)
            serializer = GetFriendSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)



        if request.method == 'POST':
            data =request.data
            serializer = CreateFriendSerializer(data=data)

            if serializer.is_valid(raise_exception=True):

                    valid_data = serializer.validated_data
                    log('VALIDATED DATA', valid_data)

                    followed_user = User.objects.only('id').get(username=valid_data['username'])
                    followed_user_id = int(followed_user.id)
                    log('FRIEND ID', followed_user_id)

                    rel_id = current_user_id + followed_user_id
                    log('REL ID', rel_id)

                    rel_exists = Following.objects.filter(current_user_id=current_user_id).filter(frd_user_id=followed_user_id).exists()
                    log('IS FRIEND REL EXISTS', rel_exists)

                    if rel_exists:
                        return Response('you already follow this user', status=status.HTTP_406_NOT_ACCEPTABLE)
                    
                    following = Following()
                    following.current_user_id = current_user_id
                    following.frd_user_if = followed_user_id
                    following.save()

                    frd_serializer = FriendSerializer(following)
                    log('FRIEND MODEL', serializer.data)
                    return Response(frd_serializer.data, status=status.HTTP_201_CREATED)
    except Exception as exec:
        return ResponseException(msg=exec)