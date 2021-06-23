import unittest
from elementretriever import ElementRetriever
from searchsetup import SearchSetUp
import threadmysoup
import os

class UnitTest(unittest.TestCase):
	@classmethod
	def setUp(self):
		urls = ['testsite.com']
		element_to_search = 'a'
		self.element_retriever = ElementRetriever(urls, element_to_search)
		self.search_setup = SearchSetUp()

	################
	# SearchSetUp class tests
	################
	def test_search_setup_has_ask_user_for_urls(self):
		self.assertTrue(hasattr(self.search_setup, 'ask_user_for_urls'))

	def test_SearchSetUp_class_has_method_in_dict(self):
		class_dict = SearchSetUp.__dict__
		self.assertTrue('ask_user_for_urls' in class_dict)

	def test_search_setup_ask_user_for_urls_returns_list(self):
		urls = self.search_setup.ask_user_for_urls()
		self.assertTrue(isinstance(urls, list))

	################
	# ElementRetriever class tests
	################
	def test_example_1(self):
		urls = ['testsite.com']
		element_to_search = 'a'
		self.assertTrue(len(urls) == 1)

	def test_element_retriever_has_urls(self):
		self.assertTrue(len(self.element_retriever.urls) == 1)

if __name__ == "__main__":
	unittest.main()
