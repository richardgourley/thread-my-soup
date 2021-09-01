class ElementFinder:
    def __init__(self):
        pass

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
                word_soup_list = list()
                soup_list = soup.find_all(['p','a','ul','li','h1','h2','h3','h4','h5'])
                for tag in soup_list:
                    tag_text = tag.get_text()
                    if word in tag_text:
                        word_soup_list.append(tag_text)
                soup_result_lists.append(word_soup_list)
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