from classes.helper.commandlineargsbase import CommandLineArgsBase

class Args(CommandLineArgsBase):
	def __init__(self):
		pass

	def return_args(self):
		command_line_args = self.get_command_line_args()

		menu_args = ["searchwords", "searchidsorclasses", "searchhtmltags"]

		if len(command_line_args) == 0:
			self.args_incorrect_message()
			quit()

		if len(command_line_args) > 1:
			self.args_incorrect_message()
			quit()

		if len(command_line_args) == 1 and command_line_args[0] in menu_args:
			print(f"You have chosen to {command_line_args[0]}")

		return command_line_args

	def args_incorrect_message(self):
		print("You need to run'threadmysoup.py' + 1 of the following menu options")
		print("EXAMPLES:")
		print("threadmysoup.py searchwords (find any words in the text)")
		print("threadmysoup.py searchidsorclasses (find elements with specific ids or classes)")
		print("threadmysoup.py searchhtmltags (find all html tags)")

