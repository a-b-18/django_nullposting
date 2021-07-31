from django.shortcuts import render

posts = [
    {
        'user_name': 'AlexBZ',
        'title': 'Fourm Post #1',
        'content': 'First conent in the forum.',
        'date_posted': 'August 31, 2018'
    },
    {
        'user_name': 'ADeBZ',
        'title': 'Fourm Post #2',
        'content': 'Serst content in the forum.',
        'date_posted': 'August 31, 2018'
    },

]

def home(request):
    context = {
        'title' : 'Home',
        'posts': posts
    }
    return render(request, 'forum/home.html', context)

def about(request):
    context = {
        'title' : 'About'
    }
    return render(request, 'forum/about.html', context)
