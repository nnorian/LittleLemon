from django.shortcuts import render
from . import views
from django.urls import path

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def home(request):
    return render(request, 'restaurant/.html') 