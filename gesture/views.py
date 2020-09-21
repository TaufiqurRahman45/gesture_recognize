from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'design/home.html')

def gesture(request):
    return render(request, 'design/gesture.html')

def question(request):
    return render(request, 'design/question.html')