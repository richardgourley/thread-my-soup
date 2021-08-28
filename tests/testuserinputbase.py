import unittest
from classes.base.userinputbase import UserInputBase

class UnitTest(unittest.TestCase):
    @classmethod
    def setUp(self):
    	self.user_input_base = UserInputBase("Enter a price", "Price cannot be blank")

    def test_enter_input_message(self):
    	self.assertEqual(self.user_input_base.enter_input_message, "Enter a price")

    def test_blank_input_message(self):
    	self.assertEqual(self.user_input_base.blank_input_message, "Price cannot be blank")

    def test_has_enter_input_message(self):
    	self.assertTrue(hasattr(self.user_input_base, "enter_input_message"))

    def test_has_blank_input_message(self):
    	self.assertTrue(hasattr(self.user_input_base, "blank_input_message"))

    def test_has_ask_user_for_inputs(self):
    	self.assertTrue(hasattr(self.user_input_base, "ask_user_for_inputs"))

    def test_has_ask_user_for_preference(self):
    	self.assertTrue(hasattr(self.user_input_base, "ask_user_for_preference"))

if __name__ == "__main__":
	unittest.main()