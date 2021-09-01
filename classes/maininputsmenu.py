from classes.base.userinputbase import UserInputBase
from classes.helper.elementfinder import ElementFinder

class MainInputsMenu(UserInputBase):
    def __init__(self, menu_option):
        self.menu_option = menu_option
        self.element_finder = ElementFinder()
        if self.menu_option == "searchwords":
            super(MainInputsMenu, self).__init__(
                "Enter a word to search in the text. Press 'Q' or 'q' to stop entering words.",
                "The word you enter cannot be blank."
            )
        if self.menu_option == "searchidsorclasses":
            super(MainInputsMenu, self).__init__(
                "Enter an id or class to search for. Press 'Q' or 'q' to stop entering classes or ids.",
                "The id or class you enter cannot be blank."
            )
        if self.menu_option == "searchhtmltags":
            super(MainInputsMenu, self).__init__(
                "Enter an html tag or element to search for. Press 'Q' or 'q' to stop entering html tags or elements.",
                "The html tag you enter cannot be blank."
            )

    def get_result_lists_based_on_menu_option(self, soup, items_to_search_for):
        if self.menu_option == "searchwords":
            result_lists = self.element_finder.find_words(soup, items_to_search_for)
            return result_lists
        elif self.menu_option == "searchidsorclasses":
            result_lists = self.element_finder.find_ids_or_classes(soup, items_to_search_for)
            return result_lists
        else:
            result_lists = self.element_finder.find_html_elements(soup, items_to_search_for)
            return result_lists





        
