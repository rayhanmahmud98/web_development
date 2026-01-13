# machine_learning/views.py
from django.shortcuts import render
from django.http import HttpResponse

def machine(request):
    
    names = {'names' : ['Rayhan', 'Mahmud', 'IIUC', 'CUET']}
    
    course = 'Data science'
    total_class = 10
    seat = 45
    course_duration = 10
    offering = {'course' : course , 'tc' : total_class , 'seat' : seat , 'cd' : course_duration }
    return render(request, 'machine_learning/machine_learning.html',context=names)

def random(request):
    return render(request, 'machine_learning/random_forest.html')

def knn(request):
    return render(request, 'machine_learning/knn.html')

def dt(request):
    return render(request, 'machine_learning/dt.html')