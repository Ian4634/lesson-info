from django.shortcuts import render
from official_use.models import Lesson, Category
from django.http import HttpResponse
from . import my_funcs
# Create your views here.
def home(request):
    categories = [ category.name for category in Category.objects.all()]
    if 'filter' in request.GET:
        for category in categories:
            if request.GET.get('filter') == category:
                context = {
                    'lessons':my_funcs.get_data(category),
                    'category':category,
                }
                return render(request, 'home.html', context)
    
    lessons = Lesson.objects.all()
    lesson_length = len(lessons)
    context = {
        'lessons':lessons,
        'lesson_length':lesson_length,
        'categories':categories,
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