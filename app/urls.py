from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('play-video/', views.single_video, name='single_video'),
    path('react-video/', views.react_video, name='react_video'),
]
