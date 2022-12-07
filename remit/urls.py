from django.urls import path
from .views import follow_view, post_view


urlpatterns = [
    path('following/', follow_view.following, name='following'),
    path('following/user/', follow_view.followed_user, name='followed_user'),
    path('posts/add/', post_view.add_post, name='add-posts'),
    path('posts/delete/', post_view.delete_post, name='delete-posts'),
    path('posts/my-posts/', post_view.get_my_posts, name='get-my-posts'),
]