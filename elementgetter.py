from threading import Thread, Lock
import requests
from bs4 import BeautifulSoup

class ElementGetter():
    def __init__(self, urls, element_to_search):
        self.urls = urls
        self.element_to_search = element_to_search
        self.results_file = "results.txt"
        self.lock = Lock()
        self.elements = None

    def start_threads(self):
        threads = [Thread(target=self.get_elements, args=(url,)) for url in self.urls]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

    def get_elements(self, url):
        self.lock.acquire()

        self.save_url_content_to_temp_file(url)
        self.get_elements_from_temp_file()
        self.append_elements_to_results_file()

        self.lock.release()

    def save_url_content_to_temp_file(self, url):
        with open('temp.txt', 'wb') as f:
            try:
                r = requests.get(url)
                if r.status_code == 200:
                    print(f"Successfully opened: {url}")
                    print("Retreiving elements")
                for chunk in r.iter_content(chunk_size=10000):
                    f.write(chunk)
            except:
                print(f"Could not open the url: {url}")

    def get_elements_from_temp_file(self):
        with open('temp.txt', 'r') as f:
            soup = BeautifulSoup(f.read(), "html.parser")
            self.elements = soup.find_all(self.element_to_search)

    def append_elements_to_results_file(self):
        with open(self.results_file, "a") as f:

            if self.element_to_search == "p":
                for el in self.elements:
                    self.append_paragraph(f, el)

                f.write("======= END OF URL =======\n")

            if self.element_to_search == "a":
                for el in self.elements:
                    self.append_link(f, el)

                f.write("======= END OF URL =======\n")

    def append_paragraph(self, f, el):
        try:
            f.write(f"{el.getText()} \n\n")
        except:
            pass

    def append_link(self, f, el):
        try:
            f.write(f"{el.getText()} - LINK: {el.attrs['href']} \n\n")
        except:
            pass

    def clear_files_content(self):
        print("Clearing files")
