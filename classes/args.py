from classes.helper.commandlineargs import CommandLineArgs

class Args:
    def __init__(self, options):
        self.command_line_args = CommandLineArgs()
        self.options = options

    def return_menu_option_or_print_args_incorrect(self):
        # removes 1st element - file name arg
        args = self.command_line_args.get_command_line_args()

        if len(args) == 0 or len(args) > 1:
            self.args_incorrect_message()
            quit()

        menu_option = self.get_menu_option(args[0], self.options)

        if menu_option is None:
            self.args_incorrect_message()
            quit() 

        print(f"You have chosen to: {menu_option['arg_full_name']}")
        
        return menu_option

    def get_menu_option(self, arg, options):
        for option in options:
            if option["arg_name"] == arg:
                return option

        return None

    def args_incorrect_message(self):
        print("You need to run 'python3' + 1 of the following menu options")
        print("EXAMPLES:")
        for arg_menu_option in self.options:
            print(f"threadmysoup.py {arg_menu_option['arg_name']} {arg_menu_option['arg_menu_description']}")
        print("----------")

