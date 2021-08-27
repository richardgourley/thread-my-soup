import unittest
from classes.base.commandlineargsbase import CommandLineArgsBase

class UnitTest(unittest.TestCase):
    @classmethod
    def setUp(self):
    	self.command_line_args_base = CommandLineArgsBase()

    def test_has_get_command_line_args(self):
        self.assertTrue(hasattr(self.command_line_args_base, "get_command_line_args"))

    def test_len_command_line_args(self):
        command_line_args = self.command_line_args_base.get_command_line_args()
        self.assertEqual(len(command_line_args), 0)
        self.assertEqual(type(command_line_args), list)

if __name__ == "__main__":
	unittest.main()