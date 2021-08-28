from classes.helper.filehandler import FileHandler
from classes.helper.threadstarter import ThreadStarter
from classes.helper.elementfinder import ElementFinder
import os

class FileSearcher:
    def __init__(self, menu_option, items_to_search_for):
        self.file_handler = FileHandler()
        self.thread_starter = ThreadStarter()
        self.element_finder = ElementFinder()
        self.add_files_message()
        self.files = self.file_handler.return_files_or_close_program()
        self.menu_option = menu_option
        self.items_to_search_for = items_to_search_for

        self.thread_starter.start_threads(self.search, self.files)
        self.search_finished_message()

    def add_files_message(self):
        print("Add any html files you want to search through to the files directory in this directory.")
        print("Press any key when you are ready!")
        any_key = input()

    # Passed to self.thread_starter.start_threads in __init__
    def search(self, file):
        self.thread_starter.lock.acquire()

        file_name = os.path.join("files", file)
        if os.path.isfile(file_name) == False:
            print(f"{file} is not a valid file. Unable to open.")
            self.thread_starter.lock.release()
            return
   
        soup = self.file_handler.parse_file(file_name)
        
        if soup == False:
            print(f"Could not retrieve data from {file_name} file.")
            self.thread_starter.lock.release()
            return
                        
        if self.menu_option == "searchwords":
            result_lists = self.element_finder.find_words(soup, self.items_to_search_for)
        elif self.menu_option == "searchidsorclasses":
            result_lists = self.element_finder.find_ids_or_classes(soup, self.items_to_search_for)
        else:
            result_lists = self.element_finder.find_html_elements(soup, self.items_to_search_for)

        if result_lists == False:
            print(f"Could not retrieve items from this file: {file}")
            self.thread_starter.lock.release()
            return
                        
        self.file_handler.append_file_results(result_lists, file_name)

        self.thread_starter.lock.release()

    def search_finished_message(self):
        print("Finished. You can find the results in a time stamped results file in the 'results' directory.")

