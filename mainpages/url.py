from django.urls import path
from . import views

app_name = 'mainpages'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('read_more/<str:lesson_id>/', views.read_more, name = 'read_more'),
    path('test/', views.test, name = 'test')
]