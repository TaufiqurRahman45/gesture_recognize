from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse

# Create your views here.
from gesture.camera import VideoCamera
from gesture.models import GestureImage


def home(request):
    gesture_images = GestureImage.objects.all()
    return render(request, 'design/home.html', {'gesture_images': gesture_images})


def gesture(request, id=None):
    gesture_image = GestureImage.objects.get(id=id)
    return render(request, 'design/gesture.html', {'gesture_image': gesture_image})


def question(request):
    return render(request, 'design/question.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_feed(request):
    return StreamingHttpResponse(gen(VideoCamera()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')
