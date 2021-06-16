from urlselector import UrlSelector
from elementgetter import ElementGetter

url_selector = UrlSelector()

# get url selection AND element to search from the user
urls = url_selector.ask_user_for_urls()
element_to_search = url_selector.ask_user_element_to_search()

element_getter = ElementGetter(urls, element_to_search)

element_getter.create_start_threads()
element_getter.clear_files_content()

print(f"The results can be found in the file: {element_getter.results_file}")







