from django.urls import path
from . import views

urlpatterns = [
    path('machine/', views.machine),
    path('dt/', views.dt),
    path('random/', views.random),
    path('knn/', views.knn),
]