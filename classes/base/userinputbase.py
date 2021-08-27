class UserInputBase:
	def __init__(self, enter_input_message, blank_input_message):
		self.enter_input_message = enter_input_message
		self.blank_input_message = blank_input_message

	def ask_user_for_inputs(self):
		inputs = []
				
		still_entering_inputs = True
		
		while still_entering_inputs:

			print(self.enter_input_message)
			user_input = input()

			if user_input == "":
				print(self.blank_input_message)
				continue

			if user_input == 'Q' or user_input == 'q':
				still_entering_inputs = False
				continue

			inputs.append(user_input)

		return inputs

	def ask_user_for_preference(self, preferences, question):
		choice = None

		choice_valid = False

		while choice_valid == False:
			print(question)

			for preference in preferences:
				print(preference)

			user_input = input()

			if user_input == "":
				print("Preference can't be blank.")
				continue

			if not user_input in preferences:
				print("Sorry please only type one of the preferences below.")
				continue

			if user_input in preferences:
				choice = "user_input"
				choice_valid = True
				continue

		print("YOU HAVE CHOSEN: ", user_input)
		return user_input
