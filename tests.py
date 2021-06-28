import unittest
from elementretriever import ElementRetriever
from searchsetup import SearchSetUp
import threadmysoup
from threading import Thread, Lock
import os

class UnitTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        # General instances of classes setup
        urls = ['']
        element_to_search = 'a'
        self.element_retriever = ElementRetriever(urls, element_to_search)
        self.search_setup = SearchSetUp()

    ################
    # SearchSetUp class tests
    ################
    def test_has_ask_user_for_urls_method(self):
        self.assertTrue(hasattr(self.search_setup, 'ask_user_for_urls'))

    def test_has_ask_urser_for_urls_method_in_dict(self):
        class_dict = SearchSetUp.__dict__
        self.assertTrue('ask_user_for_urls' in class_dict)

    def test_ask_user_for_urls_returns_list(self):
        urls = self.search_setup.ask_user_for_urls()
        self.assertTrue(isinstance(urls, list))

    ################
    # ElementRetriever class tests
    ################
    ## Methods
    def test_urls_property_has_length_1(self):
        self.assertTrue(len(self.element_retriever.urls) == 1)

    def test_has_start_threads_method(self):
        self.assertTrue(hasattr(self.element_retriever, 'start_threads'))

    def test_has_get_elements_method(self):
        self.assertTrue(hasattr(self.element_retriever, 'get_elements'))

    def test_has_get_elements_from_temp_file_method(self):
        self.assertTrue(hasattr(self.element_retriever, 'get_elements_from_temp_file'))

    def test_has_save_url_content_to_temp_file_method(self):
        self.assertTrue(hasattr(self.element_retriever, 'save_url_content_to_temp_file'))

    def test_has_get_elements_from_temp_file_method(self):
        self.assertTrue(hasattr(self.element_retriever, 'get_elements_from_temp_file'))

    def test_has_append_text_method(self):
        self.assertTrue(hasattr(self.element_retriever, 'append_text'))

    def test_has_clear_file_content_from_previous_method(self):
        self.assertTrue(hasattr(self.element_retriever, 'clear_file_content_from_previous'))

    ## Attributes
    def test_element_to_search_is_a(self):
        self.assertTrue(self.element_retriever.element_to_search == 'a')

    def test_text_elements_match(self):
        text_elements = ('h1','h2','h3','h4','h5','p','ul','li','span','title',)
        self.assertEqual(self.element_retriever.text_elements, text_elements)

    def test_has_results_file(self):
        self.assertEqual(self.element_retriever.results_file, 'results.txt')

    def test_has_lock(self):
        self.assertTrue(hasattr(self.element_retriever, 'lock'))

    ## ElementRetriever Methods
    '''def test_save_url_content_to_temp_file_returns_true(self):
                    # specific instance of ElementRetriever created - valid url in urls
                    urls = ['https://www.freecodecamp.org/']
                    element_to_search = 'a'
                    element_retriever = ElementRetriever(urls, element_to_search)
                    returned_value = element_retriever.save_url_content_to_temp_file(urls[0])
                    self.assertTrue(returned_value)'''

    def test_save_url_content_to_temp_file_returns_false(self):
        # specific instance of ElementRetriever created - invalid url in urls
        urls = ['a string not a url']
        element_to_search = 'a'
        element_retriever = ElementRetriever(urls, element_to_search)
        returned_value = element_retriever.save_url_content_to_temp_file(urls[0])
        self.assertFalse(returned_value)

    def test_get_elements_from_temp_file_returns_true(self):
        returned_value = self.element_retriever.get_elements_from_temp_file()
        self.assertTrue(returned_value)

    def test_append_elements_to_results_file(self):
        # specific instance of ElementRetriever created
        urls = ['']
        element_to_search = 'p'
        element_retriever = ElementRetriever(urls, element_to_search)
        element_retriever.elements = ['<p>Hello world</p>']
        returned_value = element_retriever.append_elements_to_results_file()
        self.assertTrue(returned_value)

    def test_append_text_returns_true(self):
        # specific instance of ElementRetriever created
        urls = ['']
        element_to_search = 'p'
        element_retriever = ElementRetriever(urls, element_to_search)

        with open('temp.txt', 'w') as temp_file:
            temp_file.write("<p>Hello</p>")

        element_retriever.get_elements_from_temp_file()
        
        results_file = open(element_retriever.results_file, 'w')

        returned_value = element_retriever.append_text(results_file, element_retriever.elements[0])

        results_file.close()

        self.assertTrue(returned_value)

    def test_append_link_returns_true(self):
        # specific instance of ElementRetriever created
        urls = ['']
        element_to_search = 'a'
        element_retriever = ElementRetriever(urls, element_to_search)

        with open('temp.txt', 'w') as temp_file:
            temp_file.write('<a href="#">Hello</a>')

        element_retriever.get_elements_from_temp_file()
        
        results_file = open(element_retriever.results_file, 'w')
        
        returned_value = element_retriever.append_link(results_file, element_retriever.elements[0])

        results_file.close()

        self.assertTrue(returned_value)


if __name__ == "__main__":
    unittest.main()
