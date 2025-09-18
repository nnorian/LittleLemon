from django.shortcuts import render
from . import views
from django.urls import path

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def home(request):
    return render(request, 'restaurant/.html') 

from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSerializer

# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer