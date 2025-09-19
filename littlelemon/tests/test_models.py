from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=60, inventory=50)
        Menu.objects.create(title="Burger", price=40, inventory=30)

    def test_getall(self):
        menus = Menu.objects.all()
        serialized_data = MenuItemSerializer(menus, many=True).data

        response = self.client.get("/restaurant/menu/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), serialized_data)