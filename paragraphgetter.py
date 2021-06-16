from threading import Thread, Lock
import requests
from bs4 import BeautifulSoup

class ParagraphGetter():
    def __init__(self, urls):
        self.urls = urls
        self.results_file = "results.txt"
        self.lock = Lock()
        self.paragraphs = None

    def create_start_threads(self):
        threads = [Thread(target=self.get_paragraphs, args=(url,)) for url in self.urls]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

    def get_paragraphs(self, url):
        self.lock.acquire()

        self.save_url_content_to_temp_file(url)
        self.get_paragraphs_from_temp_file()
        self.add_paragraphs_to_results_file()

        self.lock.release()

    def save_url_content_to_temp_file(self, url):
        with open('temp.txt', 'wb') as f:
            try:
                r = requests.get(url)
                if r.status_code == 200:
                    print(f"Successfully opened: {url}")
                    print("Retreiving paragraphs")
                for chunk in r.iter_content(chunk_size=10000):
                    f.write(chunk)
            except:
                print(f"Could not open the url: {url}")

    def get_paragraphs_from_temp_file(self):
        with open('temp.txt', 'r') as f:
            soup = BeautifulSoup(f.read(), "html.parser")
            self.paragraphs = soup.find_all('p')

    def add_paragraphs_to_results_file(self):
        with open(self.results_file, "a") as f:
            for para in self.paragraphs:
                try:
                    para_text = para.getText()
                    f.write(para_text + "\n\n")
                except:
                    pass
            f.write("======= END OF URL ========\n")

    def clear_files_content(self):
        print("Clearing files")
