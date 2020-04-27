from django.test import TestCase
from .forms import MakePaymentForm, OrderForm


class TestMakePaymentForm(TestCase):
    """test MakePaymentForm"""

    def test_form_is_valid(self):
        """test if the forms is valid"""
        payment_form = MakePaymentForm({'stripe_id': "1234567890"})
        self.assertTrue(payment_form.is_valid())

        order_form = OrderForm({'full_name': 'testuser',
                                'phone_number': '123456789',
                                'country': 'Test', 'town_or_city': 'Test',
                                'street_address1': 'street1',
                                'street_address2': 'street2',
                                'county': 'Test'})
        self.assertTrue(order_form.is_valid())

    def test_form_not_valid(self):
        """Test that our forms are not valid with empty required fields"""
        payment_form = MakePaymentForm({})
        self.assertFalse(payment_form.is_valid())
        self.assertEqual(payment_form.errors['stripe_id'],
                                            ['This field is required.'])

        order_form = OrderForm({})
        self.assertFalse(order_form.is_valid())
        self.assertEqual(order_form.errors['full_name'],
                                          ['This field is required.'])
        self.assertEqual(order_form.errors['phone_number'],
                                          ['This field is required.'])
        self.assertEqual(order_form.errors['street_address1'],
                                          ['This field is required.'])
