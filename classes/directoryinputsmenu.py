from classes.base.userinputbase import UserInputBase

class DirectoryInputsMenu(UserInputBase):
	def __init__(self, 
		enter_input_message = "Enter a directory to search.\nThe directory should start from your system root and with a slash eg. '/home/user/webprojects/portfoliosite", 
		blank_input_message = "The directory you enter must not be blank"
	):
		super(DirectoryInputsMenu, self).__init__(
			enter_input_message,
			blank_input_message 
		)
