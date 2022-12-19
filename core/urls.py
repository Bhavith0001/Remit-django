from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('', views.hello_world, name='hello-world'),
    path('register/', views.register_user, name='register-user'),
    path('login/', views.login_user, name='login-user'),
    path('current-user/', views.current_user, name='current-user'),
    path('user-list/', views.user_list, name='user-list'),
]