class ThreadMySoup:
	def __init__(self):
		pass

	def get_command_line_args(self):
		if __name__ == "__main__":
			import sys

			accepted_element_arguments = ('h1','h2','h3','h4','h5','p','a','ul','li','span','title',)
			number_arguments = len(sys.argv)

			# First argument is always the current file...

			if number_arguments == 1:
				self.print_no_arguments_added()
				quit()

			if number_arguments > 1:
				print("You have chosen to search these elements:")
				for i in range(1, number_arguments):
					print(sys.argv[i])

				return sys.argv

	def print_no_arguments_added(self):
		print("You haven't added any arguments.")
		print("Please run threadmysoup.py + 1 or more elements to search separated by a space.")
		print("EXAMPLE: 'threadmysoup.py h1 h2 h3 p a'")


threadmysoup = ThreadMySoup()
print(threadmysoup.get_command_line_args())