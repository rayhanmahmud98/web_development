# machine_learning/views.py
from django.shortcuts import render
from django.http import HttpResponse

def machine(request):
    return render(request, 'machine_learning/machine_learning.html')

def random(request):
    return render(request, 'machine_learning/random_forest.html')

def knn(request):
    return render(request, 'machine_learning/knn.html')

def dt(request):
    return render(request, 'machine_learning/dt.html')