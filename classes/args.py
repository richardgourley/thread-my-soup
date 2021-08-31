from classes.helper.commandlineargs import CommandLineArgs

class Args:
    def __init__(self):
        self.command_line_args = CommandLineArgs()

    def filter_args(self):
        # removes 1st element - file name arg
        args = self.command_line_args.get_command_line_args()

        menu_options = [
            {
                "arg":"searchwords",
                "full_name":"search for words",
            },
            {
                "arg":"searchidsorclasses",
                "full_name":"search ids or classes",
            },
            {
                "arg":"searchhtmltags",
                "full_name":"search html tags",
            },
        ]

        if len(args) == 0 or len(args) > 1:
            self.args_incorrect_message()
            quit()

        menu_option = self.get_menu_option(args[0], menu_options)

        if menu_option is None:
            self.args_incorrect_message()
            quit() 

        print(f"You have chosen to: {menu_option['full_name']}")
        
        return args

    def get_menu_option(self, arg, menu_options):
        for option in menu_options:
            if option["arg"] == arg:
                return option

        return None

    def args_incorrect_message(self):
        print("You need to run'threadmysoup.py' + 1 of the following menu options")
        print("EXAMPLES:")
        print("threadmysoup.py searchwords (find any words in the text)")
        print("threadmysoup.py searchidsorclasses (find elements with specific ids or classes)")
        print("threadmysoup.py searchhtmltags (find all html tags)")

