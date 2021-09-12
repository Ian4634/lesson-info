from django.urls import path
from . import views

app_name = 'official_use'
urlpatterns = [
    path('add_lesson/', views.add_lesson, name = 'add_lesson'),
    path('name/', views.name, name = 'name',),
    path('add_hashtag/', views.add_hashtag, name = 'add_hashtag')
]