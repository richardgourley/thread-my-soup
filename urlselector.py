class UrlSelector():
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

    

