from django.urls import path
from . import views
# from .views import 

urlpatterns = [
    path('upload/', views.upload, name='upload'),
]