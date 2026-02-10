from django.urls import path
from . import views

urlpatterns = [
    path('abs', views.about_us),
]