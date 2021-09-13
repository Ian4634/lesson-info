from django.urls import path
from . import views

app_name = 'official_use'
urlpatterns = [
    path('add_lesson/', views.add_lesson, name = 'add_lesson'),
    path('name/', views.name, name = 'name',),
    path('add_hashtag/', views.add_hashtag, name = 'add_hashtag'),
    path('', views.official_home, name = 'official_home'), 
    path('delete_lesson/<str:lesson_id>', views.delete_lesson, name = 'delete_lesson'),
    path('delete_hashtag/', views.delete_hashtag, name = 'delete_hashtag')
]