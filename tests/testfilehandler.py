import unittest
from classes.helper.filehandler import FileHandler

class UnitTest(unittest.TestCase):
    @classmethod
    def setUp(self):
    	self.file_handler = FileHandler()

    def test_append_url_results_returns_correct_file_name(self):
        pass

    def test_append_url_results_returns_correct_title_at_top_of_file(self):
        pass

    def test_append_file_results_returns_correct_file_name(self):
        pass

    def test_append_file_results_returns_correct_title_at_top_of_file(self):
        pass


if __name__ == "__main__":
	unittest.main()