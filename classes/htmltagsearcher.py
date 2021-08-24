from classes.base.threadingbase import ThreadingBase
from classes.base.filehandlerbase import FileHandlerBase
from classes.base.fileclearerbase import FileClearerBase

class HtmlTagSearcher(ThreadingBase, FileHandlerBase, FileClearerBase):
    def __init__(self, html_tags, urls, temp_file_name, results_file_name):
        super(HtmlTagSearcher, self).__init__()
        self.html_tags = html_tags
        self.urls = urls
        self.temp_file_name = temp_file_name
        self.results_file_name = results_file_name
        self.clear_results_file(self.results_file_name)
        self.clear_temp_file(self.temp_file_name)

        self.start_threads(self.search_html_tags, self.urls)

    def search_html_tags(self, url):
        self.lock.acquire()

        get_url = self.get_url_write_to_temp_file(self.temp_file_name, url)

        if get_url == False:
            print(f"Could not open the url: {url}")
            self.lock.release()
            return
        else:
            print(f"Successfully opened url: {url}")

        soup = self.parse_temp_file(self.temp_file_name)

        if soup == False:
            print(f"Could not retrieve data from the {self.temp_file_name} file.")
            self.lock.release()
            return

        result_lists = self.find_html_elements(soup, self.html_tags)

        if result_lists == False:
            print(f"Could not create result lists for this url: {url}")
            self.lock.release()
            return

        self.append_to_results_file(self.results_file_name, result_lists)

        self.lock.release()









    