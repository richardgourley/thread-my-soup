class SearchSetUp():
    def __init__(self):
        pass

    def ask_user_for_urls(self):
        urls = []

        still_entering_urls = True
        
        while still_entering_urls:
            print("Enter a valid url")
            url = input()
            if url == "":
                print("Sorry, url can't be blank.")
                continue
            urls.append(url)
            print("Enter another url? Enter 'Y' or 'N':")
            enter_another = input()
            if enter_another == 'N' or enter_another == 'n':
                still_entering_urls = False

        return urls

    def ask_user_for_element(self):
        elements = ('p', 'a')
        
        element_to_search = ""

        still_choosing_element = True

        while still_choosing_element:
            print("Which element in the page would you like to retrieve?")
            print("Enter 'p' to retrieve paragraphs")
            print("Enter 'a' to retrieve links")

            element_to_search = input()
            if element_to_search == "":
                print("Sorry, element can't be blank.")
                continue
            if not element_to_search in elements:
                print("Only enter 'p' for paragraphs, or 'a' for links.")
                continue

            still_choosing_element = False

        return element_to_search




    

