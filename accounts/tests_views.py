from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib import auth
from django.test import Client


class AccountTestsViews(TestCase):

    def setUp(self):
        user = User.objects.create(username='testuser')
        user.set_password('#Test1234')
        user.save()
        self.client = Client()
    
    def test_login_page(self):
        url = self.client.get('/accounts/login/')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, "login.html")

    def test_register_page(self):
        url = self.client.get('/accounts/register/')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, "registration.html")

    def test_user_logged_in(self):
        c = Client()
        c.login(username='testuser', password='#Test1234')
        client_user = auth.get_user(c)
        user = User.objects.get(username='testuser')
        self.assertEqual(client_user, user)

    def test_register(self):
        register = {'email': 'testaccount@example123.com',
                   'username': 'testaccount',
                   'password1': '#Test1234',
                   'password2': '#Test1234'}
        response = self.client.post('/accounts/register/', register)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/', status_code=302)

    def test_user_profile_page(self):
        url = self.client.get('/accounts/profile/')
        self.assertEqual(url.status_code, 302)
        self.assertRedirects(url, '/accounts/login/?next=/accounts/profile/',
                             status_code=302)

    def test_logging_out(self):
        url = self.client.get('/accounts/logout/')
        self.assertEqual(url.status_code, 302)
        self.assertRedirects(url, '/accounts/login/?next=/accounts/logout/',
                             status_code=302)
