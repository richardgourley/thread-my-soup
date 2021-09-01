from classes.helper.filehandler import FileHandler
from classes.helper.threadstarter import ThreadStarter

class UrlSearcher():
    def __init__(self, main_inputs_menu, items_to_search_for, urls):
        self.file_handler = FileHandler()
        self.thread_starter = ThreadStarter()
        
        self.main_inputs_menu = main_inputs_menu

        self.items_to_search_for = items_to_search_for
        self.urls = urls
        self.file_handler.clear_temp_file()

        self.file_handler.check_exists_or_make_results_dir()
        self.results_file_name = self.file_handler.create_timestamped_results_file()

        self.thread_starter.start_threads(self.search, self.urls)
        self.print_search_finished_message()

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

        result_lists = self.main_inputs_menu.get_result_lists_based_on_menu_option(soup, self.items_to_search_for)

        if result_lists == False:
            print(f"Could not create result lists for this url: {url}")
            self.thread_starter.lock.release()
            return

        self.file_handler.append_url_results(result_lists, url, self.results_file_name)

        self.thread_starter.lock.release()

    def print_search_finished_message(self):
        print("Finished. You can find the results in a time stamped results file in the 'results' directory.")