from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from core.authentication import MyAuthentication
from utils.helper import log
from ..models import Post
from utils.exceptions import ResponseException
from ..serializers.post_serializer import AddPostSerializer, PostSerializer

@api_view(http_method_names=['post'])
@authentication_classes([MyAuthentication])
def add_post(request):
    try:
        log('REQUEST', request.method)
        data = request.data
        serializer = AddPostSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.validated_data
            post = Post()
            post.user_id = request.user.id
            post.title = valid_data['title']
            post.body = valid_data['body']
            log('VALIDATED DATA', valid_data)
            post.save()
            log('POST SAVE', 'Successful')
        return Response(PostSerializer(post).data, status=status.HTTP_201_CREATED)

    except Exception as e:
        return ResponseException(msg=e)


@api_view()
@authentication_classes([MyAuthentication])
def get_my_posts(requets):
    queryset = Post.objects.filter(user_id=requets.user.id)
    serializer = PostSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(http_method_names=['delete'])
@authentication_classes([MyAuthentication])
def delete_post(request):
    try:
        Post.objects.get(user_id=request.user.id).delete()
        return Response('Post deleted successfully', status=status.HTTP_200_OK)
    except Exception as e:
        return ResponseException(msg=e)