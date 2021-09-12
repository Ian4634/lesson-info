from django.shortcuts import render
from .forms import LessonForm, CategoryForm
from .models import Lesson
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
def add_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES)
        form.save()
        return HttpResponseRedirect('?submitted=True')
    elif 'submitted' in request.GET:
        return HttpResponse('form sent')

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
        return HttpResponse('form sent')

    else:
        form = CategoryForm
        return render(request, 'add_hashtag.html', {'form':form})