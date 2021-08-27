from classes.base.threadingbase import ThreadingBase
from classes.base.filehandlerbase import FileHandlerBase
from classes.base.fileclearerbase import FileClearerBase

class UrlSearcher(ThreadingBase, FileHandlerBase, FileClearerBase):
    def __init__(self, menu_option, items_to_search_for, urls, temp_file_name, results_file_name):
        super(UrlSearcher, self).__init__()
        self.menu_option = menu_option
        self.items_to_search_for = items_to_search_for
        self.urls = urls
        self.temp_file_name = temp_file_name
        self.results_file_name = results_file_name
        self.clear_results_file(self.results_file_name)
        self.clear_temp_file(self.temp_file_name)

        self.start_threads(self.search, self.urls)

    def search(self, url):
        self.lock.acquire()

        get_url = self.get_url_write_to_temp_file(self.temp_file_name, url)

        if get_url == False:
            print(f"Could not open the url: {url}")
            self.lock.release()
            return
        else:
            print(f"Successfully opened url: {url}")

        soup = self.parse_temp_file(self.temp_file_name)

        if soup == False:
            print(f"Could not retrieve data from the {self.temp_file_name} file.")
            self.lock.release()
            return

        if self.menu_option == "searchwords":
            result_lists = self.find_words(soup, self.items_to_search_for)
        elif self.menu_option == "searchidsorclasses":
            result_lists = self.find_ids_or_classes(soup, self.items_to_search_for)
        else:
            result_lists = self.find_html_elements(soup, self.items_to_search_for)

        if result_lists == False:
            print(f"Could not create result lists for this url: {url}")
            self.lock.release()
            return

        self.append_url_results(self.results_file_name, result_lists, url)

        self.lock.release()