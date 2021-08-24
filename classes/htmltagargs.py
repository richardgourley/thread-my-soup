from classes.base.commandlineargsbase import CommandLineArgsBase

class HtmlTagArgs(CommandLineArgsBase):
	def __init__(self):
		pass

	def return_html_tag_args(self):
		command_line_args = self.get_command_line_args()

		if len(command_line_args) == 0:
			self.print_no_command_line_args_message()
			quit()

		if len(command_line_args) > 0:
			print("You have chosen to search these html tags and elements:")
			for arg in command_line_args:
				print(arg)

		return command_line_args

	def print_no_command_line_args_message(self):
		print("You haven't added any html tag or element arguments!")
		print("Please run threadmysoup.py + 1 or more tags or elements, separated by a space.")
		print("EXAMPLE: 'threadmysoup.py h1 h2 h3 p a'")

