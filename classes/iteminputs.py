from classes.base.userinputbase import UserInputBase

class ItemInputs(UserInputBase):
	def __init__(self, search_type):
		if search_type == "searchwords":
			super(ItemInputs, self).__init__(
				"Enter a word to search in the text. Press 'Q' or 'q' to stop entering words.",
				"The word you enter cannot be blank."
			)
		if search_type == "searchidsorclasses":
			super(ItemInputs, self).__init__(
				"Enter an id or class to search for. Press 'Q' or 'q' to stop entering classes or ids.",
				"The id or class you enter cannot be blank."
			)
		if search_type == "searchhtmltags":
			super(ItemInputs, self).__init__(
				"Enter an html tag or element to search for. Press 'Q' or 'q' to stop entering html tags or elements.",
				"The html tag you enter cannot be blank."
			)

		
