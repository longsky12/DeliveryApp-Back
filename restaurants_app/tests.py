from django.test import TestCase
from rest_framework.test import APIClient

class RestaurantListViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_restaurants(self):
        response = self.client.get('/restaurant/api/restaurants/')
        self.assertEqual(response.status_code,200)