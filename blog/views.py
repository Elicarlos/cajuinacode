from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'blog/index.html')
    
def blog(request):
    return render(request, 'blog/blog.html')


def contato(request):
    return render(request, 'blog/blog.html')

