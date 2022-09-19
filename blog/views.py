from django.http import HttpResponse
from django.shortcuts import render
from . models import BlogModel

# Create your views here.

def home(request):
    context = {'posts': BlogModel.objects.all()}
    return render(request, 'blog/index.html', context)

def blog(request):
    context = {'posts': BlogModel.objects.all()}
    return render(request, 'blog/blog.html', context)
    
def login_view(request):
    return render(request, 'blog/login.html')

def register_view(request):
    return render(request, 'blog/register.html')


def contato(request):
    return render(request, 'blog/blog.html')

