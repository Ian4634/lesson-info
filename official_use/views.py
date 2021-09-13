from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import LessonForm, CategoryForm
from .models import Lesson, Category
from mainpages import my_funcs
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

def official_home(request):
    return render(request, 'official_home.html')
def add_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES)
        form.save()
        return HttpResponseRedirect('?submitted=True')
    elif 'submitted' in request.GET:
        return redirect(reverse('official_use:official_home'))

    else:
        form = LessonForm
        return render(request, 'add_lesson.html', {'form':form})

def name(request):
    lesson = Lesson.objects.get(name = '小叮噹自滑')
    return HttpResponse(lesson.image.filename)

def add_hashtag(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        form.save()
        return HttpResponseRedirect('?submitted=True')
    elif 'submitted' in request.GET:
        return redirect(reverse('official_use:official_home'))

    else:
        form = CategoryForm
        return render(request, 'add_hashtag.html', {'form':form})

def official_home(request):
    categories = [ category.name for category in Category.objects.all()]
    if 'filter' in request.GET:
        for category in categories:
            if request.GET.get('filter') == category:
                context = {
                    'lessons':my_funcs.get_data(category),
                    'category':category,
                }
                return render(request, 'home.html', context)
    
    lessons = Lesson.objects.all().order_by('start_time')
    lesson_length = len(lessons)
    context = {
        'lessons':lessons,
        'lesson_length':lesson_length,
        'categories':categories,
    }
    return render(request, 'official_home.html', context)

def delete_lesson(request, lesson_id):
    Lesson.objects.get(id = lesson_id).delete()
    return redirect(reverse('official_use:official_home'))

def delete_hashtag(request):
    if request.method == 'POST':
        name = request.POST['name']
        Category.objects.get(name = name).delete()
        return redirect(reverse('official_use:official_home'))
    else:
        return render(request, 'delete_hashtag.html')