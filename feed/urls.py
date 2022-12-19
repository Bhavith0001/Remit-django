from django.urls import path
from .views import feed_posts_view, feed_post_pic_views

urlpatterns = [
    path('posts/', feed_posts_view.get_feed_posts, name='get_feed_posts'),
    path('posts/images/', feed_post_pic_views.get_post_pic_list, name='get_feed_post_pics'),
]