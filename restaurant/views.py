from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer