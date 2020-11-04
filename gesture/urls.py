from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gesture/<int:id>', views.gesture, name='gesture'),
    path('question/', views.question, name='question'),
    path('before_question/', views.before_question, name='before_question'),
    path('result/', views.result, name='result'),
    path('video_feed', views.video_feed, name='video_feed'),
]
