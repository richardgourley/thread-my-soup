from classes.base.threadingbase import ThreadingBase
from classes.base.filehandlerbase import FileHandlerBase
from classes.base.fileclearerbase import FileClearerBase
import os

class FileSearcher(ThreadingBase, FileHandlerBase, FileClearerBase):
    def __init__(self, menu_option, items_to_search_for, results_file_name):
        super(FileSearcher, self).__init__()
        print("Add any html files you want to search through to the files directory in this directory.")
        print("Press any key when you are ready!")
        any_key = input()
        self.files = self.return_files_or_close_program()
        self.menu_option = menu_option
        self.items_to_search_for = items_to_search_for
        self.results_file_name = results_file_name

        self.clear_results_file(self.results_file_name)

        self.start_threads(self.search, self.files)

    def return_files_or_close_program(self):
        directory = 'files'
        files = []
        try:
            files = os.listdir(directory)
        except:
            print("Couldn't find directory called files. We have created one. Please add files and run program again.")
            os.mkdir('trees')
            quit()

        if len(files) == 0:
            print("We could't find any files in the 'files' directory. Please add files and try again.")
            quit()

        return files

    def search(self, file):
        self.lock.acquire()

        file_name = os.path.join("files", file)
        if os.path.isfile(file_name) == False:
            print(f"{file} is not a valid file. Unable to open.")
            self.lock.release()
            return

        soup = self.parse_temp_file(file_name)

        if soup == False:
            print(f"Could not retrieve data from {file_name} file.")
            self.lock.release()
            return

        if self.menu_option == "searchwords":
            result_lists = self.find_words(soup, self.items_to_search_for)
        elif self.menu_option == "searchidsorclasses":
            result_lists = self.find_ids_or_classes(soup, self.items_to_search_for)
        else:
            result_lists = self.find_html_elements(soup, self.items_to_search_for)

        if result_lists == False:
            print(f"Could not retrieve items from this file: {file}")
            self.lock.release()
            return

        self.append_file_results(self.results_file_name, result_lists, file_name)

        self.lock.release()

