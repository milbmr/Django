from django.shortcuts import render
from .models import Post

def home(request):
    conten = {
    'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', conten)

def about(request):
    return render(request, 'blog/about.html', {'title': 'miloud'})
