from classes.helper.filehandler import FileHandler
from classes.helper.threadstarter import ThreadStarter
from classes.helper.elementfinder import ElementFinder

class UrlSearcher():
    def __init__(self, menu_option, items_to_search_for, urls):
        self.file_handler = FileHandler()
        self.thread_starter = ThreadStarter()
        self.element_finder = ElementFinder()
        self.menu_option = menu_option
        self.items_to_search_for = items_to_search_for
        self.urls = urls
        self.file_handler.clear_temp_file()

        self.thread_starter.start_threads(self.search, self.urls)
        self.search_finished_message()

    # Passed to start_threads in __init__
    def search(self, url):
        self.thread_starter.lock.acquire()

        get_url = self.file_handler.get_url_write_to_temp_file(url)

        if get_url == False:
            print(f"Could not open the url: {url}")
            self.thread_starter.lock.release()
            return
        else:
            print(f"Successfully opened url: {url}")

        soup = self.file_handler.parse_file("temp.txt")

        if soup == False:
            print(f"Could not retrieve data from the temp file.")
            self.thread_starter.lock.release()
            return

        if self.menu_option == "searchwords":
            result_lists = self.element_finder.find_words(soup, self.items_to_search_for)
        elif self.menu_option == "searchidsorclasses":
            result_lists = self.element_finder.find_ids_or_classes(soup, self.items_to_search_for)
        else:
            result_lists = self.element_finder.find_html_elements(soup, self.items_to_search_for)

        if result_lists == False:
            print(f"Could not create result lists for this url: {url}")
            self.thread_starter.lock.release()
            return

        self.file_handler.append_url_results(result_lists, url)

        self.thread_starter.lock.release()

    def search_finished_message(self):
        print("Finished. You can find the results in a time stamped results file in the 'results' directory.")