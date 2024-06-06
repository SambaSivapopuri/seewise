from django.urls import path
from .views import *
urlpatterns = [
    path('register/', UserRegistration.as_view(), name='user-registration'),
    path('login/', UserLogin.as_view(), name='user-login'),
    path('user-home/', UserHome.as_view(), name='user-home'), 
    path('', VideoListCreate.as_view(), name='video-list-create'),
    path('<int:pk>/', VideoDetail.as_view(), name='video-detail'),
    path('<int:pk>/stream/', video_feed, name='video-feed'),
    path('search/', VideoSearch.as_view(), name='video-search'),
]
