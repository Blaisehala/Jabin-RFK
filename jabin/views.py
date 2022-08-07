from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'users/home.html')

def about(request):
    return render(request, 'users/about.html')

def programs(request):
    return render(request, 'users/programs.html')

def data(request):
    return render(request, 'users/data.html')

def contact(request):
    return render(request, 'users/contact.html')