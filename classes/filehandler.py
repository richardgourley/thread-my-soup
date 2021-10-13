from bs4 import BeautifulSoup

class FileHandler:
    def __init__(self):
        pass

    def parse_file(self, file_name):
        try:
            with open(file_name, "r") as file:
                soup = BeautifulSoup(file.read(), "html.parser")
                return soup
        except:
            return None

    def append_to_results_file(self, result_lists, retrieved_file, results_file_name):
        with open(results_file_name, "a") as file:
            for result_set in result_lists:
                for el in result_set:
                    file.write(str(el) + "\n\n")
            file.write(f"==== END OF {retrieved_file} ====\n\n")