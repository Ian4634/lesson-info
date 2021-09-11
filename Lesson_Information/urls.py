
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mainpages/', include('mainpages.url')),
    path('official_use', include('official_use.url'))
]
