import unittest
from classes.args import Args
from classes.helper.elementfinder import ElementFinder

class UnitTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        element_finder = ElementFinder()
        menu_options = [
            {
                'arg_name':'searchwords',
                'arg_full_name':'Search Words',
                'arg_menu_description':'(find matching words in the text of elements)',
                'enter_input_message':"Enter a word to search in the text. Press 'Q' or 'q' to stop entering words.",
                'blank_input_message':"The word you enter cannot be blank.",
                'search_function':element_finder.find_words
            },
            {
                'arg_name':'searchidsorclasses',
                'arg_full_name':'Search Ids or Classes',
                'arg_menu_description':'(find elements with matching ids or classes)',
                'enter_input_message':"Enter a class or id to search for. Press 'Q' or 'q' to stop entering ids or classes.",
                'blank_input_message':"The class or id name you enter cannot be blank.",
                'search_function':element_finder.find_ids_or_classes
            },
            {
                'arg_name':'searchhtmltags',
                'arg_full_name':'Search HTML tags',
                'arg_menu_description':'(find all matching html tags)',
                'enter_input_message':"Enter an html tag to search for. Press 'Q' or 'q' to stop entering html elements.",
                'blank_input_message':"The html tag name you enter cannot be blank.",
                'search_function':element_finder.find_html_elements
            }
        ]
        self.args = Args(menu_options)

    def test_has_return_menu_option_or_print_args_incorrect(self):
        self.assertTrue(hasattr(self.args, "return_menu_option_or_print_args_incorrect"))

    def test_has_get_menu_option(self):
        self.assertTrue(hasattr(self.args, "get_menu_option"))

    def test_has_args_incorrect_message(self):
        self.assertTrue(hasattr(self.args, "args_incorrect_message"))

    # Pass an 'arg_full_name' from menu options in setUp
    def test_get_menu_option_returns_option_from_menu_options(self):
        arg = "searchhtmltags"
        result = self.args.get_menu_option(arg, self.args.options)
        self.assertEqual(result['arg_full_name'], 'Search HTML tags')
        self.assertEqual(result['arg_menu_description'], '(find all matching html tags)')
        self.assertEqual(result['enter_input_message'], "Enter an html tag to search for. Press 'Q' or 'q' to stop entering html elements.")

    def test_get_menu_option_returns_none_for_incorrect_menu_option(self):
        arg = "hello, world!"
        result = self.args.get_menu_option(arg, self.args.options)
        self.assertEqual(result, None)


