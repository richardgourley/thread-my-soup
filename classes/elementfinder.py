from threading import Thread, Lock
import requests
from bs4 import BeautifulSoup

class ElementFinder:
    def __init__(self, html_elements_to_find, urls_to_search):
        self.html_elements_to_find = html_elements_to_find
        self.urls_to_search = urls_to_search
        self.lock = Lock()

    def start_threads(self):
        self.clear_results_file_from_previous_search()

        # A thread started for each url in 'self.urls_to_search'
        threads = [Thread(target=self.find_html_elements_and_save_results, args=(url,)) for url in self.urls_to_search]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

    def find_html_elements_and_save_results(self, url):
        self.lock.acquire()
        
        soup = False
        soup_result_sets = False

        if self.write_url_binary_source_code_to_temp_file(url):
            soup = self.convert_temp_file_to_beautiful_soup_class()

        if soup:
            soup_result_lists = self.find_html_elements_and_create_result_lists(soup)

        if soup_result_lists:
            self.append_to_results_file(soup_result_lists)

        self.lock.release()

    def write_url_binary_source_code_to_temp_file(self, url):
        with open('temp.txt', 'wb') as file:
            try:
                r = requests.get(url)
                if r.status_code == 200:
                    print(f"Successfully opened url: {url}")
                    print("Retreiving elements")
                for chunk in r.iter_content(chunk_size=10000):
                    file.write(chunk)
                return True
            except:
                print(f"Could not open the url: {url}")
                return False

    def convert_temp_file_to_beautiful_soup_class(self):
        try:
            with open('temp.txt', 'r') as file:
                soup = BeautifulSoup(file.read(), "html.parser")
                return soup
        except:
            print("Could not retrieve elements.")
            return False

    def find_html_elements_and_create_result_lists(self, soup):
        soup_result_lists = list()

        try:
            for element in self.html_elements_to_find:
                soup_result_lists.append(soup.find_all(element))
            return soup_result_lists
        except:
            print("Could not retrieve html elements")
            return False

    def append_to_results_file(self, soup_result_lists):
        with open("results.txt", "a") as file:
            for result_set in soup_result_lists:
                for el in result_set:
                    file.write(str(el) + "\n\n")
            file.write("==== END OF URL ====\n\n")

    def clear_results_file_from_previous_search(self):
        with open("results.txt", "w") as file:
            file.write("")


