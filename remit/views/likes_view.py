from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from rest_framework import status
from core.authentication import MyAuthentication
from ..models import Post
from core.models import User
from utils.exceptions import ResponseException


@api_view(http_method_names=['post', 'delete'])
@authentication_classes([MyAuthentication])
def like_post(request, post_id):
    try:
        user_id = request.user.id
        post = Post.objects.get(pk=post_id)

        if request.method == 'POST':
            """ likes the post """
            post.likes.add(User.objects.get(pk=user_id).id)
            return Response({'response': 'liked'}, status=status.HTTP_200_OK)
        
        if request.method == 'DELETE':
            """ unlikes the post """
            post.likes.remove(User.objects.get(pk=user_id).id)
            return Response({'response': 'unliked'})

    except Exception as e:
        return ResponseException(msg=e)