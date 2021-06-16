from urlselector import UrlSelector
from elementgetter import ElementGetter

url_selector = UrlSelector()

urls = url_selector.ask_user_for_urls()
element_to_search = url_selector.ask_user_for_element()

element_getter = ElementGetter(urls, element_to_search)

element_getter.clear_file_content_from_previous()
element_getter.start_threads()

print(f"The results can be found in the file: {element_getter.results_file}")







