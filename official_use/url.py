from django.urls import path
from . import views

urlpatterns = [
    path('add_lesson/', views.add_lesson, name = 'add_lesson')
]