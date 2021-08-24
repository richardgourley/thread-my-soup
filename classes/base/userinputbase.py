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
