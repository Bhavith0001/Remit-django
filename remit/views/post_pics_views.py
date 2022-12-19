from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from core.authentication import MyAuthentication
from utils.helper import log
from ..models import PostPicture
from ..serializers.post_pic_serializers import CurrentUserPostPicSerializer


@api_view(http_method_names=['post'])
@authentication_classes([MyAuthentication])
def upload_picture(request):
    log('INSIDE', 'before first if condtion')
    if request.method == 'POST':
        data = request.data
        serializer = CurrentUserPostPicSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            log('INSIDE', 'first if condtion')
            valid_data = serializer.validated_data
            post_pic = PostPicture()
            post_pic.user = request.user
            post_pic.caption = valid_data['caption']
            post_pic.post_image = valid_data['post_image']
            post_pic.save()
            serializer = CurrentUserPostPicSerializer(post_pic)
            return Response(serializer.data)


@api_view(http_method_names=['get'])
@authentication_classes([MyAuthentication])
def get_my_pic_posts(request):
    queryset = PostPicture.objects.filter(user_id=request.user.id).all()
    serializer = CurrentUserPostPicSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(http_method_names=['delete'])
@authentication_classes([MyAuthentication])
def delete_post_pic(request, pk):
    post_pic = PostPicture.objects.filter(user_id=request.user.id).get(pk=pk)
    post_pic.post_image.delete()
    post_pic.delete()
    return Response('deleted successfully', status=status.HTTP_204_NO_CONTENT)


@api_view(http_method_names=['post', 'delete'])
@authentication_classes([MyAuthentication])
def like_post_pic(request, post_pic_id):
    post_pic = PostPicture.objects.get(pk=post_pic_id)

    if request.method == 'POST':
        post_pic.likes.add(request.user.id)
        return Response('liked')

    if request.method == 'DELETE':
        post_pic.likes.remove(request.user.id)
        return Response('unliked')