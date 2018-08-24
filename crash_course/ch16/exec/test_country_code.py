
import unittest


from country_codes import get_country_code


class CountryCodesTestCase(unittest.TestCase):
    """Tests for 'country_codes.py'"""

    def test_get_country_code(self):
        """test for get_country_code"""
        cc = get_country_code('Australia')
        self.assertEqual(cc, 'au')


unittest.main()
