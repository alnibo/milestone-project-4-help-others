from django.test import TestCase, Client
from .views import do_search
from projects.models import Project
from django.contrib import auth
from django.contrib.auth.models import User


class TestSearch(TestCase):
    """test the search function"""
    def setUp(self):
        self.user = User.objects.create_user(username="testuser",
                                             password="#Test1234")
        self.client.login(username="testuser", password="#Test1234")

    def test_loading_search_page(self):
        self.user = User.objects.get(username="testuser")
        self.project = Project(name="test")
        self.project.save()
        url = self.client.get('/search/?q=test')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'projects.html')
