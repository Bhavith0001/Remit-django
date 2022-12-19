from django.urls import path
from .views import follow_view, post_view, post_pics_views, likes_view, profile_img_views


urlpatterns = [
    path('following/', follow_view.following, name='following'),
    path('user/', follow_view.get_user, name='get-user'),
    path('user/<user_id>/', follow_view.follow_or_unfollow, name='follow-or-unfollow'),

    path('posts/add/', post_view.add_post, name='add-posts'),
    path('posts/my-posts/', post_view.get_my_posts, name='get-my-posts'),
    path('posts/like/<post_id>/', likes_view.like_post, name='like-post'),
    path('posts/delete/<post_id>/', post_view.delete_post, name='delete-posts'),

    path('posts/images/add/', post_pics_views.upload_picture, name='add-post-pic'),
    path('posts/my-images/', post_pics_views.get_my_pic_posts, name='my-post-pic'),
    path('posts/my-images/delete/<int:pk>/', post_pics_views.delete_post_pic, name='delete-post-pic'),
    path('posts/images/like/<post_pic_id>/', post_pics_views.like_post_pic, name='like-post-pic'),

    path('profile/image/', profile_img_views.profile_pic, name='profile_image'),
]