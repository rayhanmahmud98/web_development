from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def machine(request):
    return HttpResponse('Welcome to the FIGHT CLUB')

def deep_learning(request):
    return HttpResponse('Welcome to Deep Learning')

def About_Us(request):
    return HttpResponse('We are open to be Acknowledged')