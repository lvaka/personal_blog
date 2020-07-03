"""Core Routes Tests."""
from django.test import TestCase


class CoreTestCase(TestCase):
    """Test Routes."""

    def test_home_route(self):
        """Get home and return response 200."""
        client = self.client
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_route(self):
        """Get about and return response 200."""
        client = self.client
        response = client.get('/about')
        self.assertEqual(response.status_code, 200)
