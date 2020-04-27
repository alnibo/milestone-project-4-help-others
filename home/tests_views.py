from django.test import TestCase


class MyTest(TestCase):

    def test_loading_index(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('index.html')
    
    def test_loading_about_us(self):
        response = self.client.get('/about_us/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('about.html')
