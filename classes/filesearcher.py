from classes.helper.filehandler import FileHandler
from classes.helper.threadstarter import ThreadStarter
import os

class FileSearcher:
    def __init__(self, menu_option, items_to_search_for, directory_to_search="files"):
        self.file_handler = FileHandler()
        self.thread_starter = ThreadStarter()
        self.directory_to_search = directory_to_search
        self.menu_option = menu_option
        self.items_to_search_for = items_to_search_for

        self.print_add_files_message()

        if directory_to_search == "files":
            self.files = self.file_handler.return_files_from_files_dir_or_close_program()
        else:
            self.files = self.file_handler.return_files_from_other_dir_or_close_program(self.directory_to_search)

        self.file_handler.check_exists_or_make_results_dir()
        self.results_file_name = self.file_handler.create_timestamped_results_file()

        self.thread_starter.start_threads(self.search, self.files)
        self.print_search_finished_message()

    def print_error_stop_thread(self, obj, error_message):
        if obj == False:
            print(error_message)
            self.thread_starter.lock.release()
            return True
        return False

    def stop_thread_invalid_file(self, file):
        try:
            is_file = os.path.isfile(file)
            if is_file == False:
                print(f"{file} is not a valid file. Unable to open.")
                self.thread_starter.lock.release()
                return True
            return False
        except:
            print(f"{file} is not a valid file. Unable to open.")
            self.thread_starter.lock.release()
            return True


    # Passed to self.thread_starter.start_threads in __init__
    def search(self, file):
        self.thread_starter.lock.acquire()

        if self.stop_thread_invalid_file(file) == True:
            return
        
        soup = self.file_handler.parse_file(file)

        if self.print_error_stop_thread(soup, f"Unable to parse the file {file}") == True:
            return 

        # search functions per menu_option found in classes.helper.elementretriever
        result_lists = self.menu_option['search_function'](soup, self.items_to_search_for)

        if self.print_error_stop_thread(result_lists, f"Unable to retrieve results from the file: {file}") == True:
            return
                        
        self.file_handler.append_file_results(result_lists, file, self.results_file_name)

        self.thread_starter.lock.release()

    def print_search_finished_message(self):
        print("Finished. You can find the results in a time stamped results file in the 'results' directory.")

    def print_add_files_message(self):
        print(f"\nWe will search through any html files found in the directory called '{self.directory_to_search}' AND any sub-directories.")
        print(f"Please check your website project files and directories are in the directory: '{self.directory_to_search}'.")
        print("Press any key when you are ready!")
        any_key = input()

