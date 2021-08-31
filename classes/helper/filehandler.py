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
            with open(file_name, 'r') as file:
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
    def return_files_or_close_program(self):
        directory = 'files'
        files = []
        try:
            files = os.listdir(directory)
        except:
            print("Couldn't find directory called files. We have created one. Please add files and run program again.")
            os.mkdir('files')
            quit()

        if len(files) == 0:
            print("We could't find any files in the 'files' directory. Please add files and try again.")
            quit()

        return files

    def clear_temp_file(self):
        with open("temp.txt", "w") as file:
            file.write("")

