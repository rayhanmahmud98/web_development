from django.urls import path
from . import views

urlpatterns = [
    path('abs/', views.about_us,name='about'),
    path('t/',views.teachers_info,name = 'tinfo' )
]