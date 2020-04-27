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
