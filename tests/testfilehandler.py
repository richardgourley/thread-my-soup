import unittest
import os
from classes.filehandler import FileHandler

class UnitTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.file_handler = FileHandler()
        with open('unittest.html', 'w') as file:
            file.write(
                "<p class='text-secondary'>Hello, world!</p>\n<ul><li>Section 1</li></ul>"
            )

    def test_parse_file_returns_soup(self):
        file_name = 'unittest.html'
        soup = self.file_handler.parse_file(file_name)
        paragraphs = soup.find_all('p')
        self.assertTrue(soup, 'find_all')
        self.assertEqual(str(paragraphs[0].getText()), "Hello, world!")


if __name__ == "__main__":
    unittest.main()
