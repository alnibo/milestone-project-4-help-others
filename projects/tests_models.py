from django.test import TestCase
from projects.models import Project


class ProjectTest(TestCase):
    """
    Here all tests are defined that
    are run against the Project models
    """

    def test_str(self):
        project = Project(name='Test Project')
        self.assertEqual(str(project), 'Test Project')
    
    def test_add_project(self):
        project = Project(name='Test', category='Test Cat',
                          description='Test Desc')
        project.save()
        self.assertEqual(project.name, "Test")
        self.assertEqual(project.category, "Test Cat")
        self.assertEqual(project.description, "Test Desc")
