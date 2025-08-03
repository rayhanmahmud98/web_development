from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    context = {'page':'home'}
    
    peoples = [
    {'name': 'rayhan', 'age': 26},
    {'name': 'sarah', 'age': 14},
    {'name': 'alex', 'age': 30},
    {'name': 'gg','age': 15},
    {'name': 'michael', 'age': 28}
]
    

    
    return render(request,"index.html", context = {'peoples' : peoples})

def success_page(request):
    return HttpResponse("Congratulation for your success!!!!!!!!!!")

def about(request):
    context = {'page':'About'}
    return render(request,"about.html",context)

def contact(request):
    context = {'page':'Contact'}
    return render(request,"contact.html",context)