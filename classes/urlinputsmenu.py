from classes.base.userinputbase import UserInputBase

class UrlInputsMenu(UserInputBase):
	def __init__(self, 
		enter_input_message = "Enter a url to search. Press 'Q' or 'q' to stop entering urls.", 
		blank_input_message = "The url you enter must not be blank"
	):
		super(UrlInputsMenu, self).__init__(
			enter_input_message,
			blank_input_message 
		)
