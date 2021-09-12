from django.shortcuts import render
from official_use.models import Lesson
# Create your views here.
def home(request):
    lessons = Lesson.objects.all()
    lesson_length = len(lessons)
    context = {
        'lessons':lessons,
        'lesson_length':lesson_length,
    }
    return render(request, 'home.html', context)