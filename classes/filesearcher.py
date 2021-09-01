from classes.helper.filehandler import FileHandler
from classes.helper.threadstarter import ThreadStarter
import os

class FileSearcher:
    def __init__(self, main_inputs_menu, items_to_search_for):
        self.file_handler = FileHandler()
        self.thread_starter = ThreadStarter()

        self.main_inputs_menu = main_inputs_menu

        self.print_add_files_message()
        self.files = self.file_handler.return_files_or_close_program()

        self.items_to_search_for = items_to_search_for

        self.file_handler.check_exists_or_make_results_dir()
        self.results_file_name = self.file_handler.create_timestamped_results_file()

        self.thread_starter.start_threads(self.search, self.files)
        self.print_search_finished_message()

    def print_add_files_message(self):
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

        result_lists = self.main_inputs_menu.get_result_lists_based_on_menu_option(soup, self.items_to_search_for)

        if result_lists == False:
            print(f"Could not retrieve items from this file: {file}")
            self.thread_starter.lock.release()
            return
                        
        self.file_handler.append_file_results(result_lists, file_name, self.results_file_name)

        self.thread_starter.lock.release()

    def print_search_finished_message(self):
        print("Finished. You can find the results in a time stamped results file in the 'results' directory.")

