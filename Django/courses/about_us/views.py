# about_us/views.py
from django.http import HttpResponse
from django.shortcuts import render

def about_us(request):
    # Include the "about/" subdirectory
    return render(request, 'about/about_us.html')