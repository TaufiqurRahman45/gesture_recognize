from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gesture/',views.gesture, name= 'gesture'),
    path('question/',views.question, name= 'question'),
]