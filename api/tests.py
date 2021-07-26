from django.test import TestCase
from rest_framework.test import APIClient
from .models import User


class ProfileTest(TestCase):
    def setUp(self):
        self.api_client = APIClient()
        self.user = User.objects.create(
            username='nikita',
            password='123',
        )
        self.super_user = User.objects.create(
            username='nikita1',
            password='123',
            is_staff=True
        )

    def test_user_get(self):
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.get('/api/v1/users/')
        self.assertEqual(response.status_code, 200)

        response = self.api_client.get(f'/api/v1/users/{self.user.id}/')
        self.assertEqual(response.status_code, 200)

    def test_user_post(self):
        new_user = {
            'username': 'nikita',
            'password': '123',
        }
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.post('/api/v1/users/')
        self.assertEqual(response.status_code, 403)

        self.api_client.force_authenticate(user=self.super_user)
        response = self.api_client.post('/api/v1/users/', new_user)
        self.assertEqual(response.status_code, 400)

    def test_user_patch(self):
        new_data = {
            'username': 'nikita34',
        }
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.patch(f'/api/v1/users/{self.user.id}/', new_data)
        self.assertEqual(response.status_code, 200)
