from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

class APITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_api_root(self):
        response = self.client.get(reverse('api_notice_list'))
        self.assertEqual(response.status_code, 401)  # Unauthorized without login
