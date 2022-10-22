
from http.client import REQUEST_ENTITY_TOO_LARGE
import re
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from . models import BlogModel
from . forms import CommentForm

# Create your views here.

def home(request):
    context = {
        'posts': BlogModel.objects.all()
    }
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

def post_detail(request, slug): 
    post = get_object_or_404(BlogModel, slug=slug)

    if request.method == 'POST':  
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            form.save()
            return redirect('post_detail', slug=slug)
    
    else: 
        form = CommentForm()    
    return render(request, 'blog/post.html', {'post': post, 'form': form })

