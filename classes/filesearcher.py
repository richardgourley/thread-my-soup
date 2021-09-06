from classes.helper.filehandler import FileHandler
from classes.helper.threadstarter import ThreadStarter
import os

class FileSearcher:
    def __init__(self, main_inputs_menu, items_to_search_for, directory_to_search="files directory"):
        self.file_handler = FileHandler()
        self.thread_starter = ThreadStarter()

        self.directory_to_search = directory_to_search

        self.main_inputs_menu = main_inputs_menu

        self.print_add_files_message()

        if directory_to_search == "files":
            self.files = self.file_handler.return_files_from_files_dir_or_close_program()
        else:
            self.files = self.file_handler.return_files_from_other_dir_or_close_program(self.directory_to_search)

        self.items_to_search_for = items_to_search_for

        self.file_handler.check_exists_or_make_results_dir()
        self.results_file_name = self.file_handler.create_timestamped_results_file()

        self.thread_starter.start_threads(self.search, self.files)
        self.print_search_finished_message()

    def print_add_files_message(self):
        print(f"\nWe will search through any html files found in the directory called '{self.directory_to_search}' AND any sub-directories.")
        print(f"Please check your website project files and directories are in the directory: '{self.directory_to_search}'.")
        print("Press any key when you are ready!")
        any_key = input()

    # Passed to self.thread_starter.start_threads in __init__
    def search(self, file):
        self.thread_starter.lock.acquire()

        if os.path.isfile(file) == False:
            print(f"{file} is not a valid file. Unable to open.")
            self.thread_starter.lock.release()
            return
   
        soup = self.file_handler.parse_file(file)
        
        if soup == False:
            print(f"Could not retrieve data from {file} file.")
            self.thread_starter.lock.release()
            return

        result_lists = self.main_inputs_menu.get_result_lists_based_on_menu_option(soup, self.items_to_search_for)

        if result_lists == False:
            print(f"Could not retrieve items from this file: {file}")
            self.thread_starter.lock.release()
            return
                        
        self.file_handler.append_file_results(result_lists, file, self.results_file_name)

        self.thread_starter.lock.release()

    def print_search_finished_message(self):
        print("Finished. You can find the results in a time stamped results file in the 'results' directory.")

