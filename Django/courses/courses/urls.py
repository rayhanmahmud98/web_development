"""
URL configuration for courses project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from machine_learning.views import machine
from machine_learning.views import deep_learning
from machine_learning.views import About_Us
from Blogs.views import blogs1
from data_analysis.views import data_analysis
from deep_learning.views import deep_learning
from about_us.views import about_us



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',machine),
    path('about_us/',About_Us),
    path('blogs/',blogs1),
    path('da/',data_analysis),
    path('dl/',deep_learning),
    path('abs/',about_us),
]
