from django.http import HttpResponse
from django.shortcuts import render
from . forms import TeachersRegistration

# Create your views here.

def blog1(request):
    # Include the "blog/" subdirectory
    return render(request, 'blog/blogs.html')

def ShowFormsData(request):
    fm = TeachersRegistration()
    return render(request,'blog/forms.html',{'form': fm})