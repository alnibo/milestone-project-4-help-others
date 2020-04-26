from django.test import TestCase
from .models import Project

class ProjectTest(TestCase):
    """
    Here all tests are defined that
    are run against the Project models
    """

    def test_str(self):
        test_name = Project(name='Test Project')
        test_user = Project(added_by='user')
        self.assertEqual(str(test_name, test_user), 'Test Project user')
