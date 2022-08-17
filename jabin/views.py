from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from jabin.models import Order 


# Create your views here.

def home(request):
    return render(request, 'users/home.html')

def about(request):
    return render(request, 'users/about.html')

def programs(request):
    return render(request, 'users/programs.html')

def data(request):
    return render(request, 'users/data.html')

def pivot_data(request):
    dataset= Order.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)

def contact(request):
    return render(request, 'users/contact.html')