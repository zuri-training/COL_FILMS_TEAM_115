from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('play-video/', views.single_video, name='single_video'),
    path('react-video/', views.react_video, name='react_video'),
    path('share-video/', views.share_video, name='share_video'),
    path('save-video/', views.save_video, name='save_video'),
    path('fetch-saved-video/', views.fetch_saved_video, name='fetch_saved_video'),
    path('comment-video/', views.comment, name='comment'),
    path('home/', views.home, name='home'),
]
