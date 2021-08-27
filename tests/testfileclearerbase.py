import unittest
from classes.base.fileclearerbase import FileClearerBase

class UnitTest(unittest.TestCase):
    @classmethod
    def setUp(self):
    	self.file_clearer_base = FileClearerBase()

    def test_has_clear_results_file(self):
    	self.assertTrue(hasattr(self.file_clearer_base, "clear_results_file"))

    def test_has_blank_input_message(self):
    	self.assertTrue(hasattr(self.file_clearer_base, "clear_temp_file"))

    def test_clear_results_file_works(self):
        with open("results.txt", "w") as file:
            file.write("hello, world")
        self.file_clearer_base.clear_results_file("results.txt")
        with open("results.txt", "r") as file:
            lines = file.readlines()
        self.assertEqual(len(lines), 0)

    def test_clear_temp_file_works(self):
        with open("temp.txt", "w") as file:
            file.write("hello, world")
        self.file_clearer_base.clear_temp_file("temp.txt")
        with open("temp.txt", "r") as file:
            lines = file.readlines()
        self.assertEqual(len(lines), 0)


if __name__ == "__main__":
	unittest.main()