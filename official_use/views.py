from django.shortcuts import render
from .forms import LessonForm
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