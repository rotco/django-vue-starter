from django.test import TestCase, Client
from django.urls import reverse
from .models import User
import json


class UserViewsTestCase(TestCase):
    def setUp(self):
        self.user_data = {"name": "Haim Moshe", "address": "Laskov 50 Holon"}
        self.user = User.objects.create(**self.user_data)
        self.client = Client()

    def test_filtered_user_ids_view(self):
        url = reverse("filtered-users")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("results", response.json())

    def test_user_list_view(self):
        url = reverse("users")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("results", response.json())

    def test_user_list_post_valid_data(self):
        url = reverse("users")
        response = self.client.post(
            url, data=json.dumps(self.user_data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("results", response.json())

    def test_user_list_post_invalid_data(self):
        url = reverse("users")
        invalid_data = {"name": ""}
        response = self.client.post(
            url, data=json.dumps(invalid_data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("errors", response.json())

    def test_user_delete_view(self):
        url = reverse("user-delete", args=[self.user.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())
