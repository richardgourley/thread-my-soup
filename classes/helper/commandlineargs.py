import sys

class CommandLineArgs:
	def __init__(self):
		pass

	def get_command_line_args(self):
		command_line_args = list(sys.argv)

		if len(command_line_args) > 0:
			# First arg is always the current file name - not required 
			command_line_args.pop(0)

		return command_line_args