from classes.helper.commandlineargs import CommandLineArgs

class Args:
	def __init__(self):
		self.command_line_args = CommandLineArgs()

	def return_args(self):
		args = self.command_line_args.get_command_line_args()

		menu_args = ["searchwords", "searchidsorclasses", "searchhtmltags"]

		if len(args) == 0:
			self.args_incorrect_message()
			quit()

		if len(args) > 1:
			self.args_incorrect_message()
			quit()

		if len(args) == 1 and args[0] in menu_args:
			print(f"You have chosen to {args[0]}")

		return args

	def args_incorrect_message(self):
		print("You need to run'threadmysoup.py' + 1 of the following menu options")
		print("EXAMPLES:")
		print("threadmysoup.py searchwords (find any words in the text)")
		print("threadmysoup.py searchidsorclasses (find elements with specific ids or classes)")
		print("threadmysoup.py searchhtmltags (find all html tags)")

