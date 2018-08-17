
import unittest

from city_functions import city_country


class CityTestCase(unittest.TestCase):
    """Test case for 'city_functions.py'"""

    def test_city_country(self):
        """Do like 'Santiago, Chile' work?"""
        formatted_name = city_country('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do like 'Santiago, Chile - population 5000000'"""
        formatted_name = city_country('santiago', 'chile', 5000000)
        self.assertEqual(formatted_name, 'Santiago, Chile - population 5000000')


unittest.main()
