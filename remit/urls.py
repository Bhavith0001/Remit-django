from django.urls import path
from .views import friends_view, post_view


urlpatterns = [
    path('friends/', friends_view.friends, name='friend'),
    path('posts/add/', post_view.add_post, name='add-posts'),
    path('posts/my-posts/', post_view.get_my_posts, name='get-my-posts'),
    path('feed/posts/', post_view.feed_posts, name='feed-posts'),
]