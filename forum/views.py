from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Forum Please</h1>')

def about(request):
    return HttpResponse('<h1>About Please</h1>')
