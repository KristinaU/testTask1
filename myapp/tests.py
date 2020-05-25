from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class UserTest(APITestCase):
    def test_registration(self):
        url = reverse('registration')
        data = {'TestUser'}
        response = self.client.post(url, data, format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
