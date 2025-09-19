#define Serializer class for User model
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class BookingViewSet(viewset.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

