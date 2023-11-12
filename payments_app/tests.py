from rest_framework.test import APITestCase
from django.urls import reverse

class PaymentViewSetTest(APITestCase):
    def test_payment_approval(self):
        _url = reverse('payment-approval')
        _data = {'pg_token':'sample_pg_token'}

        response = self.client.post(_url,_data,format='json')

        self.assertEqual(response.status_code,200)
        self.assertIn('result',response.data)