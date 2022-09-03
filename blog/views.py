from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'blog/index.html')
    
def blog(request):
<<<<<<< HEAD
    return HttpResponse('Blog')
=======
    return render(request, 'Blog/blog.html')
>>>>>>> 501aeba684a9ab171a52d8e35e01436d6331eb1e
