import unittest
import os
from classes.directoryvalidation import DirectoryValidation

class UnitTest(unittest.TestCase):
	@classmethod
	def setUp(self):
		self.directory_validation = DirectoryValidation()
		current_dir = os.getcwd()

	def test_incorrect_dir_returns_false(self):
		is_dir_valid = self.directory_validation.validate_directory("/home/incorrect/path/testing")
		self.assertFalse(is_dir_valid)

if __name__ == "__main__":
	unittest.main()