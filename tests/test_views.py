from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()

        # Create test data
        self.menu1 = MenuItem.objects.create(Title="Pizza", Price=9.99, Inventory=10)
        self.menu2 = MenuItem.objects.create(Title="Burger", Price=5.49, Inventory=15)
        self.menu3 = MenuItem.objects.create(Title="Salad", Price=4.99, Inventory=5)

    def test_getall(self):
        # Get all menu items from the API
        response = self.client.get('/restaurant/menu/') # Replace 'menu-list' with your actual URL name

        # Get all menu items from the DB
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)