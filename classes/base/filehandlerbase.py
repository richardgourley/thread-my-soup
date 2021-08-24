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

    def find_html_elements(self, soup, html_elements_to_find):
        soup_result_lists = list()

        try:
            for element in html_elements_to_find:
                soup_result_lists.append(soup.find_all(element))
            return soup_result_lists
        except:
            return False

    def append_to_results_file(self, results_file_name, soup_result_lists):
        with open(results_file_name, "a") as file:
            for result_set in soup_result_lists:
                for el in result_set:
                    file.write(str(el) + "\n\n")
            file.write("==== END OF URL ====\n\n")

