import unittest
from elementretriever import ElementRetriever
from searchsetup import SearchSetUp
import threadmysoup
import os

class UnitTest(unittest.TestCase):
	@classmethod
	def setUp(self):
		print("UnitTest setup")
		pass

	def test_example_1(self):
		print("I am test example 1")
		self.assertTrue(5 * 5 == 23)

if __name__ == "__main__":
	unittest.main()
