# machine_learning/views.py
from django.shortcuts import render
from django.http import HttpResponse

def machine(request):
    return render(request, 'machine_learning.html')