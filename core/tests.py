"""Core Routes Tests."""
from django.test import TestCase


class IndexTestCase(TestCase):
    """Get Index Page."""

    def test_get_route(self):
        """Get Route and return response 200."""
        client = self.client
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
