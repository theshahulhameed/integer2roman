#from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse


class HomepageTests(SimpleTestCase):
    '''
    Tests to ensure the homepage returns
    expected status code and the URL name is
    correct.
    '''

    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
