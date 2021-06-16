from urlselector import UrlSelector
from paragraphgetter import ParagraphGetter

urlselector = UrlSelector()

# get url selection from user, passed as parameter to paragraph_getter
urls = urlselector.ask_user_for_urls()

paragraph_getter = ParagraphGetter(urls)

paragraph_getter.create_start_threads()
paragraph_getter.clear_files_content()

print(f"The results can be found in the file: {paragraph_getter.results_file}")








