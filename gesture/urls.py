from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gesture/<int:id>', views.gesture, name='gesture'),
    path('question/', views.question, name='question'),
    path('video_feed', views.video_feed, name='video_feed'),
]
