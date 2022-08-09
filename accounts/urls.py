from django.urls import path
from . import views
import accounts

app_name = 'accounts'
urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
