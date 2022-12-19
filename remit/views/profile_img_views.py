from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from core.authentication import MyAuthentication
from utils.helper import log
from utils.exceptions import ResponseException
from ..models import ProfileImage
from ..serializers.profile_pic_serializers import ProfilePicSerializer


@api_view(http_method_names=['get','post', 'put', 'delete'])
@authentication_classes([MyAuthentication])
def profile_pic(request):
    current_user_id = request.user.id

    try:

        if request.method == 'GET':
            profile_pic = ProfileImage.objects.get(user_id=current_user_id)
            return Response(ProfilePicSerializer(profile_pic).data, status=status.HTTP_200_OK)

        if request.method == 'POST':
            data = request.data
            serializer = ProfilePicSerializer(data=data)

            if serializer.is_valid(raise_exception=True):
                valid_data = serializer.validated_data
                if ProfileImage.objects.filter(user_id=current_user_id).exists():
                    raise ValueError('Cannot POST image for this user, please use PUT method to update')
                profile_pic = ProfileImage()
                profile_pic.user_id = current_user_id
                profile_pic.image = valid_data['image']
                profile_pic.save()
            return Response(ProfilePicSerializer(profile_pic).data, status=status.HTTP_200_OK)


        if request.method == 'PUT':
            data = request.data
            serializer = ProfilePicSerializer(data=data)

            if serializer.is_valid():
                valid_data = serializer.validated_data
                profile_pic = ProfileImage.objects.get(user_id=current_user_id)
                profile_pic.image.delete()

                profile_pic.user_id = current_user_id
                profile_pic.image = valid_data['image']
                profile_pic.save()
            return Response(ProfilePicSerializer(profile_pic).data, status=status.HTTP_200_OK)
        

        if request.method == 'DELETE':
            profile_pic = ProfileImage.objects.get(user_id=current_user_id)
            profile_pic.image.delete()
            profile_pic.delete()
            return Response('Deleted succussfully', status=status.HTTP_404_NOT_FOUND)
    
    except Exception as e:
        return ResponseException(msg=e)