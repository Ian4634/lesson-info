from django.urls import path
from . import views

app_name = 'mainpages'
urlpatterns = [
    path('', views.home, name = 'home')
]