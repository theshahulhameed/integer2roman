from django.test import SimpleTestCase
from django.urls import reverse
from pages.utils import integerToRoman


class HomepageTests(SimpleTestCase):
    '''
    Django specific tests to ensure the homepage returns
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


class IntegerToRomanTests(SimpleTestCase):
    '''
    Test to ensure the utility function we created
    gives expected results for the inputs
    '''

    def test_with_input_as_four(self):
        input = 4
        result = integerToRoman(input)
        self.assertNotEqual(result, 'IIII')

    def test_input_less_than_five(self):
        input = 4
        result = integerToRoman(input)
        self.assertEqual(result, 'IV')

    def test_with_input_as_three(self):
        input = 3
        result = integerToRoman(input)
        self.assertEqual(result, 'III')

    def test_with_input_as_nine(self):
        input = 9
        result = integerToRoman(input)
        self.assertEqual(result, 'IX')

    def test_with_input_as_thirty_seven(self):
        input = 37
        result = integerToRoman(input)
        self.assertEqual(result, 'XXXVII')

    def test_with_input_as_ninteeen_ninety_three(self):
        input = 1993
        result = integerToRoman(input)
        self.assertEqual(result, 'MCMXCIII')

    def test_bad_type(self):
        data = "apple"
        with self.assertRaises(TypeError):
            result = integerToRoman(data)
