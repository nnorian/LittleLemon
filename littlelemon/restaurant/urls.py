#define URL route for index() view
# restaurant/urls.py
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    
]