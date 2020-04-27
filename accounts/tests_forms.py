from django.test import TestCase
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegistrationForm

def setUp(self):
        user = User.objects.create(username='testuser')
        user.set_password('#Test1234')
        user.save()


class AccountTestsLoginForm(TestCase):
    """Testing the login form """
    
    def test_login_form_valid_data(self):
        user = {'username': 'testuser', 'password': '#Test1234'}
        form = UserLoginForm(data=user)
        self.assertTrue(form.is_valid)

    def test_login_form_invalid_data(self):
        form = UserLoginForm(data={'username': '', 'password': ''})
        self.assertEqual(form.errors,
                         {'username': ['This field is required.'],
                          'password': ['This field is required.']})


class AccountTestsRegisterForm(TestCase):
    """Testing the register form """

    def test_successfull_register(self):
        form = UserRegistrationForm({'username': "testuser",
                                     "password1": "#Test1234",
                                     "password2": "#Test1234",
                                     "email": "testaccount@example123.com"})
        self.assertTrue(form.is_valid())

    def test_register_with_existing_username(self):
        setUp(self)
        form = UserRegistrationForm({'username': "testuser",
                                     "password1": "#Test1234",
                                     "password2": "#Test1234",
                                     "email": "testaccount@example123.com"})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'],
                                    ['A user with that username already exists.'])

    def test_matching_passwords(self):
        form = UserRegistrationForm({'username': 'testuser',
                                     'password1': '#Test1234',
                                     'password2': '#Test4321'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'password2': ['Passwords must match']})

    def test_required_fields(self):
        form = UserRegistrationForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors,
                         {'username': ['This field is required.'],
                          'password1': ['This field is required.'],
                          'password2': ['This field is required.']})
