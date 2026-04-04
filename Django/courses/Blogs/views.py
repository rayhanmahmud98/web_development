from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def blog1(request):
    # Include the "blog/" subdirectory
    return render(request, 'blog/blogs.html')