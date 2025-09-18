#define URL route for index() view
# restaurant/urls.py
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),  # this should match a function in views.py
]