from rest_framework.decorators import api_view, authentication_classes
from rest_framework import status
from rest_framework.response import Response
from core.models import User
from core.authentication import MyAuthentication
from core.serializers import UserSerializer
from ..models import Following
from ..serializers.follow_serializers import CreateFollowSerializer, FollowSerializer, GetFollowSerializer
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

            queryset = Following.objects.filter(current_user_id=current_user_id)
            serializer = GetFollowSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)



        if request.method == 'POST':
            """ follow user """
            data =request.data
            serializer = CreateFollowSerializer(data=data)

            if serializer.is_valid(raise_exception=True):

                valid_data = serializer.validated_data
                log('VALIDATED DATA', valid_data)

                follow_user_id = User.objects.only('id').get(username=valid_data['username']).id
                log('FOLLOWER ID', follow_user_id)

                rel_exists = Following.objects.filter(current_user_id=current_user_id).filter(follow_user_id=follow_user_id).exists()
                log('IS FOLLOW REL EXISTS', rel_exists)

                if rel_exists:
                    return Response('you already follow this user', status=status.HTTP_406_NOT_ACCEPTABLE)
                
                following = Following()
                following.current_user_id = current_user_id
                following.follow_user_id = follow_user_id
                following.save()

                follow_serializer = FollowSerializer(following)
                log('FOLLOWING MODEL', serializer.data)
                return Response(follow_serializer.data, status=status.HTTP_201_CREATED)


    except Exception as exec:
        return ResponseException(msg=exec)



@api_view(http_method_names=['get', 'delete'])
@authentication_classes([MyAuthentication])
def followed_user(request):
    try:
        data = request.data
        serializer = CreateFollowSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.validated_data
            
            current_user_id = request.user.id
            follow_user = User.objects.get(username=valid_data['username'])
            log('DELETE USER ID', follow_user)
            
            follow_user_id = follow_user.id
            log('DELETE USER ID', follow_user_id)
            following = Following.objects.filter(current_user_id=current_user_id).get(follow_user_id=follow_user_id)

            if request.method == 'GET':
                serializer = UserSerializer(follow_user)
                return Response(serializer.data, status=status.HTTP_200_OK)

            if request.method == 'DELETE':
                """ unfollow user """
                following.delete()
                return Response('Unfollowed Successfully', status=status.HTTP_200_OK)

    except Exception as e:
        return ResponseException(msg=e)