import unittest
from bs4 import BeautifulSoup
from datetime import datetime
import os

from classes.elementfinder import ElementFinder

class UnitTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.element_finder = ElementFinder()
        with open('unittest.html', 'w') as file:
            file.write(
                "<p class='text-secondary'>Hello, world!</p>\n<ul><li>Section 1</li></ul>"
            )

    def test_find_html_elements(self):
        soup = None
        with open('unittest.html', 'r') as file:
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

    # if html_elements_to_find is not iterable 
    def test_find_html_elements_returns_none(self):
        soup = None
        with open('unittest.html', 'r') as file:
            soup = BeautifulSoup(file.read(), "html.parser")
        html_elements_to_find = 34.5
        soup_result_list = self.element_finder.find_html_elements(soup, html_elements_to_find)
        self.assertEqual(soup_result_list, None)

    def tearDown(self):
        pass




if __name__ == "__main__":
    unittest.main()