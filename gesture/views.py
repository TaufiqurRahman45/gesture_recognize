from django.shortcuts import render, redirect
from django.http import HttpResponse, StreamingHttpResponse

# Create your views here.
from django.urls import reverse

from gesture.camera import VideoCamera
from gesture.models import GestureImage

ANSWERS = {
    'A': 5,
    'B': 4,
    'C': 3.5,
    'D': 2,
    'E': 1,
}


def home(request):
    gesture_images = GestureImage.objects.all()
    return render(request, 'design/home.html', {'gesture_images': gesture_images})


def gesture(request, id=None):
    gesture_image = GestureImage.objects.get(id=id)
    return render(request, 'design/gesture.html', {'gesture_image': gesture_image})


def before_question(request):
    if "point" in request.session.keys():
        del request.session["point"]
    if "actual_time" in request.session.keys():
        del request.session["actual_time"]
    if "taken_time" in request.session.keys():
        del request.session["taken_time"]

    if request.method == "POST" and request.POST.get('type', '') == 'gesture':
        data = request.POST
        request.session['actual_time'] = data['actual_time']
        request.session['taken_time'] = data['taken_time']

    return redirect(reverse('question'))


def question(request):
    if request.method == "POST" and request.POST.get('type', '') == 'answers':
        data = request.POST
        point = ANSWERS[data['question-1-answers']]
        point += ANSWERS[data['question-2-answers']]
        point += ANSWERS[data['question-3-answers']]
        point += ANSWERS[data['question-4-answers']]
        point += ANSWERS[data['question-5-answers']]
        point += ANSWERS[data['question-6-answers']]
        point += ANSWERS[data['question-7-answers']]
        request.session['point'] = point

        return redirect(reverse('result'))
    return render(request, 'design/question.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_feed(request):
    return StreamingHttpResponse(gen(VideoCamera()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')


def result(request):
    if "point" not in request.session.keys() and "actual_time" not in request.session.keys() and "taken_time" not in request.session.keys():
        return redirect(reverse('home'))

    context = {
        'point': request.session.get('point', 0),
        'actual_time': request.session.get('actual_time', 0),
        'taken_time': request.session.get('taken_time', 0),
    }
    return render(request, "design/result.html", context)
