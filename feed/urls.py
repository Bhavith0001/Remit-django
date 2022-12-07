from django.urls import path
from .views import feed_posts_view

urlpatterns = [
    path('posts/', feed_posts_view.get_feed_posts, name='get_feed_posts'),
]