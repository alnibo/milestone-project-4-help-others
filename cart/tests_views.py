from django.test import TestCase


class TestCart(TestCase):
    """test cart view"""

    def test_loading_cart(self):
        page = self.client.get('/cart/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'cart.html')
