from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all
    }
    return render(request, 'forum/home.html', context)

def about(request):
    context = {
        'title' : 'About'
    }
    return render(request, 'forum/about.html', context)
