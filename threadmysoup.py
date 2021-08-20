from classes.elementretriever import ElementRetriever

class ThreadMySoupSetUp:
    def __init__(self):
        pass

    def get_command_line_html_element_args(self):
        if __name__ == "__main__":
            import sys

            #accepted_element_arguments = ('h1','h2','h3','h4','h5','p','a','ul','li','span','title',)
            
            command_line_args = list(sys.argv)

            # First argument is always the current file...
            command_line_args.pop(0)

            number_arguments = len(command_line_args)

            if number_arguments == 0:
                self.print_no_arguments_added()
                quit()

            if number_arguments > 0:
                print("You have chosen to search these elements:")
                for arg in command_line_args:
                    print(arg)

                return command_line_args

    def ask_user_for_urls_to_search(self):
        urls = []

        still_entering_urls = True
        
        while still_entering_urls:
            print("Enter a url to find the html elements in.")
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

    def print_no_arguments_added(self):
        print("You haven't added any arguments.")
        print("Please run threadmysoup.py + 1 or more elements to search separated by a space.")
        print("EXAMPLE: 'threadmysoup.py h1 h2 h3 p a'")


thread_my_soup = ThreadMySoupSetUp()
html_elements_to_find = thread_my_soup.get_command_line_html_element_args()
urls_to_search = thread_my_soup.ask_user_for_urls_to_search()

element_retriever = ElementRetriever(
        html_elements_to_find,
        urls_to_search
    )
