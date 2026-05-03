# about_us/views.py
from django.http import HttpResponse
from django.shortcuts import render
from about_us.models import Teachers

def about_us(request):
    # Include the "about/" subdirectory
    return render(request, 'about/about_us.html')

def teachers_info(request):
    teach = Teachers.objects.all()
    return render (request,'about/teachers.html',{'thr':teach})