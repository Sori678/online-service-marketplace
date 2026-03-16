from django.test import TestCase
from .models import Service
from django.contrib.auth.models import User

class MarketplaceViewsTest(TestCase):
    """
    Basic tests for the marketplace application.
    """
    def setUp(self):
        """
        Create a test user and a test service.
        """
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpassword'
        )
        self.service = Service.objects.create(
            title='Test Service',
            provider=self.user,
            description='Test Description',
            category='it',
            price=10.00
        )

    def test_service_list_view(self):
        """
        Test if the service list page loads correctly.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Service')

    def test_service_detail_view(self):
        """
        Test if the service detail page loads correctly.
        """
        response = self.client.get(f'/service/{self.service.id}/')
        # Dacă URL-ul tău e diferit, ajustează calea de mai sus
        self.assertEqual(response.status_code, 200)