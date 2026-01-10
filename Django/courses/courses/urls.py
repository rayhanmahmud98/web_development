# courses/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # Add this

def home_test(request):
    return HttpResponse("HOME PAGE TEST - Django is working!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ml/', include('machine_learning.urls')),
    path('dl/', include('deep_learning.urls')),
    path('about/', include('about_us.urls')),
    path('blogs/', include('Blogs.urls')),
    path('da/', include('data_analysis.urls')),
]