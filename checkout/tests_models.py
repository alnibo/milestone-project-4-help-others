from django.test import TestCase
from .models import Order


class TestCheckoutModel(TestCase):

    def test_string_sample(self):
        order = Order(full_name="testuser", phone_number="123456789",
                      street_address1="street1", postcode="12345")
        self.assertEqual(str(order.full_name), order.full_name)
