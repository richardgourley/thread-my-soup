from classes.elementfinder import ElementFinder

class ThreadMySoupSetUp:
	def __init__(self):
		pass

	def get_command_line_html_element_args(self):
		if __name__ == "__main__":
			import sys

			command_line_args = list(sys.argv)

			# Remove first arg -> because first arg is always the current file name
			command_line_args.pop(0)

			number_arguments = len(command_line_args)

			if number_arguments == 0:
				self.print_no_command_line_arguments_added()
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

	def print_no_command_line_arguments_added(self):
		print("You haven't added any html element arguments!")
		print("Please run threadmysoup.py + 1 or more elements to search separated by a space.")
		print("EXAMPLE: 'threadmysoup.py h1 h2 h3 p a'")


thread_my_soup = ThreadMySoupSetUp()
html_elements_to_find = thread_my_soup.get_command_line_html_element_args()
urls_to_search = thread_my_soup.ask_user_for_urls_to_search()

element_finder = ElementFinder(
		html_elements_to_find,
		urls_to_search
	)

element_finder.start_threads()
