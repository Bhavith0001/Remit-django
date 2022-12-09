from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('user-list/', views.user_list, name='user_list'),
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('current-user/', views.current_user, name='current_user'),
    path('hello/', views.hello_world, name='hello_world'),
    path('', views.hello_world),
]