from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_home.as_view(), name="home"),
    path('signup/', views.view_signup, name='signup'),
    path('signin/', views.view_signin, name='signin'),
    path('create/', views.view_create, name='create'),
]