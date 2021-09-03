import unittest
from bs4 import BeautifulSoup
from datetime import datetime
import os

from classes.helper.filehandler import FileHandler

class UnitTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.file_handler = FileHandler()
        self.unittest_file = 'tests/unittest.html'
        with open(self.unittest_file, 'w') as file:
            file.write(
                "<p class='text-secondary'>Hello, world!</p>\n<ul><li>Section 1</li></ul>"
            )

    def test_parse_file_returns_beautifulsoup_instance(self):
        soup = self.file_handler.parse_file(self.unittest_file)
        self.assertEqual(type(soup),  BeautifulSoup)

    def test_create_timestamped_results_file_returns_string(self):
        date_now = datetime.now()
        results_file = self.file_handler.create_timestamped_results_file()
        self.assertIs(type(results_file), str)

    def test_create_timestampled_results_file_contains_todays_date(self):
        date_now = datetime.now()
        results_file = self.file_handler.create_timestamped_results_file()
        self.assertTrue(str(date_now.hour) in results_file)
        self.assertTrue(str(date_now.minute) in results_file)
        self.assertTrue(str(date_now.day) in results_file)
        self.assertTrue(str(date_now.month) in results_file)

    def test_return_files_or_close_program(self):
        # make sure 'files' dir exist or program will close on running method
        directory = 'files'
        try:
            files = os.listdir(directory)
        except:
            os.mkdir('files')
            quit()
        files = self.file_handler.return_files_or_close_program()
        self.assertEqual(type(files), list)

    def test_clear_temp_file_works(self):
        self.file_handler.clear_temp_file()
        opened_file = ""
        with open('temp.txt', 'r') as file:
            opened_file = file.read()
        self.assertEqual(len(opened_file), 0)

if __name__ == "__main__":
    unittest.main()