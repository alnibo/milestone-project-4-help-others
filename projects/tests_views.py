from django.test import TestCase, Client
from django.contrib import auth
from django.contrib.auth.models import User
from projects.models import Project
from django.shortcuts import get_object_or_404

class test_project_pages(TestCase):

    def setUp(self):
        self.client = Client()

    """Test if view of all projects works"""
    def test_loading_all_projects(self):
        page = self.client.get('/projects/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'projects.html')

    """Test if category view works"""
    def test_loading_category(self):
        page = self.client.get('/projects/Animals/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'projects.html')

    """Test if project detail view works"""
    def test_loading_project_details(self):
        project = Project.objects.create(
            name="A project", category="Test", description="Test"
        )
        response = self.client.get(f"/projects/{project.id}")
        self.assertEqual(response.status_code, 200)

    """Log in user to view the add project page"""
    def setUp(self):
        self.user = User.objects.create_user(username="testuser",
                                             password="#Test1234")
        self.client.login(username="testuser", password="#Test1234")

    """Test if add project view works"""
    def test_loading_add_project(self):
        page = self.client.get('/projects/add_project/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'add_project.html')
