from django.test import TestCase
from django.contrib import auth
from django.contrib.auth.models import User


class TestCheckout(TestCase):

    """Log in user to view the checkout page"""
    def setUp(self):
        self.user = User.objects.create_user(username="testuser",
                                             password="#Test1234")
        self.client.login(username="testuser", password="#Test1234")

    """Test checkout view"""
    def test_loading_checkout_page(self):
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout.html')
