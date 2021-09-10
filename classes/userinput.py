from classes.base.userinputbase import UserInputBase

class UserInput(UserInputBase):
    def __init__(self, option):
        self.option = option
        super(UserInput, self).__init__(
            option['enter_input_message'],
            option['blank_input_message']
        )