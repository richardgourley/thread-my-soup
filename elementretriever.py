from threading import Thread, Lock
import requests
from bs4 import BeautifulSoup

class ElementRetriever():
    def __init__(self, urls, element_to_search):
        self.urls = urls
        self.element_to_search = element_to_search
        self.text_elements = ('h1','h2','h3','h4','h5','p','ul','li','span','title',)
        self.href_elements = ('a',)
        self.results_file = "results.txt"
        self.lock = Lock()
        # Assigned in method 'get_elements_from_temp_file'
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
        with open('temp.txt', 'wb') as file:
            try:
                r = requests.get(url)
                if r.status_code == 200:
                    print(f"Successfully opened: {url}")
                    print("Retreiving elements")
                for chunk in r.iter_content(chunk_size=10000):
                    file.write(chunk)
                return True
            except:
                print(f"Could not open the url: {url}")
                return False

    def get_elements_from_temp_file(self):
        with open('temp.txt', 'r') as file:
            soup = BeautifulSoup(file.read(), "html.parser")
            self.elements = soup.find_all(self.element_to_search)

    def append_elements_to_results_file(self):
        with open(self.results_file, "a") as file:

            if self.element_to_search in self.text_elements:
                for element in self.elements:
                    self.append_text(file, element)

                file.write("======= END OF URL =======\n")

            if self.element_to_search in self.href_elements:
                for element in self.elements:
                    self.append_link(file, element)

                file.write("======= END OF URL =======\n")

    def append_text(self, file, element):
        try:
            file.write(f"{element.getText()} \n\n")
        except:
            pass

    def append_link(self, file, element):
        try:
            file.write(f"{element.getText()} - LINK: {element.attrs['href']} \n\n")
        except:
            pass

    def clear_file_content_from_previous(self):
        with open('results.txt', 'w') as file:
            file.write("")
        with open('temp.txt', 'w') as file:
            file.write("")

