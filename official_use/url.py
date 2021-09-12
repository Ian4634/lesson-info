from django.urls import path
from . import views

app_name = 'official_use'
urlpatterns = [
    path('add_lesson/', views.add_lesson, name = 'add_lesson'),
    path('name/', views.name, name = 'name',)
]