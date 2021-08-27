import requests
from bs4 import BeautifulSoup

class FileHandlerBase:
    def __init__():
        pass

    def get_url_write_to_temp_file(self, temp_file_name, url):
        with open(temp_file_name, 'wb') as file:
            try:
                r = requests.get(url)
                if r.status_code == 200:
                    for chunk in r.iter_content(chunk_size=10000):
                        file.write(chunk)
                return True
            except:
                return False

    def parse_temp_file(self, temp_file_name):
        try:
            with open(temp_file_name, 'r') as file:
                soup = BeautifulSoup(file.read(), "html.parser")
                return soup
        except:
            return False

    ## Finder methods
    def find_html_elements(self, soup, html_elements_to_find):
        soup_result_lists = list()

        try:
            for element in html_elements_to_find:
                soup_result_lists.append(soup.find_all(element))
            return soup_result_lists
        except:
            return False

    def find_words(self, soup, words_to_find):
        soup_result_lists = list()

        try:
            for word in words_to_find:
                updated_soup_list = list()
                soup_list = soup.find_all()
                for line in soup_list:
                    if word in line.getText():
                        updated_soup_list.append(line)
                soup_result_lists.append(updated_soup_list)
            return soup_result_lists
        except:
            return False

    def find_ids_or_classes(self, soup, ids_or_classes_to_find):
        soup_result_lists = list()

        try:
            for item in ids_or_classes_to_find:
                soup_result_lists.append(soup.find_all(id=item))
                soup_result_lists.append(soup.find_all(class_=item))
            return soup_result_lists
        except:
            return False

    ## Append to results.txt methods
    def append_url_results(self, results_file_name, result_lists, url):
        with open(results_file_name, "a") as file:
            for result_set in result_lists:
                for el in result_set:
                    file.write(str(el) + "\n\n")
            file.write(f"==== END OF URL: {url} ====\n\n")

    def append_file_results(self, results_file_name, result_lists, file_name):
        with open(results_file_name, "a") as file:
            for result_set in result_lists:
                for el in result_set:
                    file.write(str(el) + "\n\n")
            file.write(f"==== END OF {file_name} ====\n\n")

