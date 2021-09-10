import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

class FileHandler:
    def __init__(self):
        pass

    def get_url_write_to_temp_file(self, url):
        with open("temp.txt", 'wb') as file:
            try:
                r = requests.get(url)
                if r.status_code == 200:
                    for chunk in r.iter_content(chunk_size=10000):
                        file.write(chunk)
                return True
            except:
                return False

    def parse_file(self, file_name):
        try:
            with open(file_name, "r") as file:
                soup = BeautifulSoup(file.read(), "html.parser")
                return soup
        except:
            return False

    ## Append to results.txt methods
    def append_url_results(self, result_lists, url, results_file_name):
        with open(results_file_name, "a") as file:
            for result_set in result_lists:
                for el in result_set:
                    file.write(str(el) + "\n\n")
            file.write(f"==== END OF URL: {url} ====\n\n")

    def append_file_results(self, result_lists, file_name, results_file_name):
        with open(results_file_name, "a") as file:
            for result_set in result_lists:
                for el in result_set:
                    file.write(str(el) + "\n\n")
            file.write(f"==== END OF {file_name} ====\n\n")

    ## Creates results file, create results dir if required
    def create_timestamped_results_file(self):
        date_now = datetime.now()
        results_file = f"results/results_{date_now.month}_{date_now.day}_{date_now.year}_{date_now.hour}:{date_now.minute}.{date_now.second}.txt"
        return results_file

    def check_exists_or_make_results_dir(self):
        try:
            files = os.listdir("results")
        except:
            print("Couldn't find directory called results. We have created one. Please add files and run program again.")
            os.mkdir('results')
            quit()

    ## Returns files to FileSearcher class or exits program.
    def return_files_from_files_dir_or_close_program(self):
        output_files = []

        try:
            current_dir = os.getcwd()
            search_dir = os.path.join(current_dir, 'files')

            for main_dir, sub_dir, files in os.walk(search_dir):
                for file in files:
                    try:
                        name, extension = os.path.splitext(file)
                        if extension == ".html":
                            file_address = f"{main_dir}/{file}"
                            output_files.append(file_address)
                    except:
                        pass
        except:
            print("Couldn't find directory called files. We have created one. Please add files and/ or directories to 'files' and run the program again.")
            os.mkdir('files')
            quit()

        if len(output_files) == 0:
            print(f"We could't find any html files in the 'files' directory. Please check there are files and directories with html files and try again.")
            quit()

        return output_files

    def return_files_from_other_dir_or_close_program(self, directory_to_search):
        output_files = []

        try:
            search_dir = os.path.relpath(directory_to_search)

            for main_dir, sub_dir, files in os.walk(search_dir):
                for file in files:
                    try:
                        name, extension = os.path.splitext(file)
                        if extension == ".html":
                            file_address = f"{main_dir}/{file}"
                            print(file_address)
                            output_files.append(file_address)
                    except:
                        pass
        except:
            print(f"Couldn't find directory called {directory_to_search}.Please check the directory address is correct and run the program again.")
            quit()

        if len(output_files) == 0:
            print(f"We could't find any html files in the {directory_to_search} directory. Please check the directory address is correct and that there are files and directories with html files inside and try again.")
            quit()

        return output_files

    def clear_temp_file(self):
        with open("temp.txt", "w") as file:
            file.write("")


