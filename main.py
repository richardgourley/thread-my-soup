from urlselector import UrlSelector
from paragraphgetter import ParagraphGetter

url_selector = UrlSelector()

# get url selection AND element to search from the user
urls = url_selector.ask_user_for_urls()
element_to_search = url_selector.ask_user_element_to_search()

paragraph_getter = ParagraphGetter(urls, element_to_search)

paragraph_getter.create_start_threads()
paragraph_getter.clear_files_content()

print(f"The results can be found in the file: {paragraph_getter.results_file}")







