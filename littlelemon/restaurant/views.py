from django.shortcuts import render
from . import views
from rest_framework.decorators import permission_classes
from django.urls import path
from rest_framework import generics
from rest_framework.permissions  import IsAuthenticated
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def home(request):
    return render(request, 'restaurant/.html') 


# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewset.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
