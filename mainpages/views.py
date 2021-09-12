from django.shortcuts import render
from official_use.models import Lesson
from django.http import HttpResponse
# Create your views here.
def home(request):
    lessons = Lesson.objects.all()
    lesson_length = len(lessons)
    context = {
        'lessons':lessons,
        'lesson_length':lesson_length,
    }
    return render(request, 'home.html', context)

def read_more(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    context = {
        'lesson':lesson,
    }
    return render(request, 'read_more.html', context)

def test(request):
    return render(request, 'test.html')