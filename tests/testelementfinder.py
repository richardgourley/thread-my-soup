import unittest
from bs4 import BeautifulSoup
from datetime import datetime
import os

from classes.helper.elementfinder import ElementFinder

class UnitTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.element_finder = ElementFinder()
        self.unittest_file = 'tests/unittest.html'
        with open(self.unittest_file, 'w') as file:
            file.write(
                "<p class='text-secondary'>Hello, world!</p>\n<ul><li>Section 1</li></ul>"
            )

    def test_find_html_elements(self):
        soup = None
        with open(self.unittest_file, 'r') as file:
            soup = BeautifulSoup(file.read(), "html.parser")
        html_elements_to_find = ['p','li']
        soup_result_list = self.element_finder.find_html_elements(soup, html_elements_to_find)
        self.assertEqual(len(soup_result_list), 2)
        self.assertEqual(type(soup_result_list), list)
        self.assertEqual(len(soup_result_list[0]), 1)
        self.assertEqual(soup_result_list[0][0].get_text(), 'Hello, world!')
        self.assertEqual(soup_result_list[0][0].name, 'p')
        self.assertEqual(soup_result_list[1][0].get_text(), 'Section 1')
        self.assertEqual(soup_result_list[1][0].name, 'li')




if __name__ == "__main__":
    unittest.main()