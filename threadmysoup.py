from classes.args import Args
from classes.userinput import UserInput
from classes.filesearcher import FileSearcher
from classes.helper.elementfinder import ElementFinder

if __name__ == "__main__":
	element_finder = ElementFinder()

	menu_options = [
		{
			'arg_name':'searchwords',
			'arg_full_name':'Search Words',
			'arg_menu_description':'(find matching words in the text of elements)',
			'enter_input_message':"Enter a word to search in the text. Press 'Q' or 'q' to stop entering words.",
			'blank_input_message':"The word you enter cannot be blank.",
			'search_function':element_finder.find_words
		},
		{
			'arg_name':'searchidsorclasses',
			'arg_full_name':'Search Ids or Classes',
			'arg_menu_description':'(find elements with matching ids or classes)',
			'enter_input_message':"Enter a class or id to search for. Press 'Q' or 'q' to stop entering ids or classes.",
			'blank_input_message':"The class or id name you enter cannot be blank.",
			'search_function':element_finder.find_ids_or_classes
		},
		{
			'arg_name':'searchhtmltags',
			'arg_full_name':'Search HTML tags',
			'arg_menu_description':'(find all matching html tags)',
			'enter_input_message':"Enter an html tag to search for. Press 'Q' or 'q' to stop entering html elements.",
			'blank_input_message':"The html tag name you enter cannot be blank.",
			'search_function':element_finder.find_html_elements
		}
	]

	# Args menu - search words, search ids or classes, search html tags?
	args = Args(menu_options)
	menu_option = args.return_menu_option_or_print_args_incorrect()

	# User inputs words, ids, classes or html tags to search
	user_input = UserInput(menu_option)
	items_to_search_for = user_input.ask_user_for_inputs()

	# User chooses which directory to traverse - 'files' dir OR another directory
	search_files_dir_or_other_dir = user_input.ask_user_for_preference(
		["files", "other"], 
		"Enter an option below - would you like to search through all files and sub-directories in the 'files' directory or search through a different directory on your system?\nEnter 'files directory or 'other directory'"
	)

	if search_files_dir_or_other_dir == "files":
		file_searcher = FileSearcher(
			menu_option,
			items_to_search_for,
		)
	else:
		directory_input_menu = UserInput(
			{
				"enter_input_message":"Enter a directory to search.\nThe directory should start from your system root and with a slash eg. '/home/user/webprojects/portfoliosite", 
				"blank_input_message":"The directory you enter must not be blank"
			}
		)
		directory_to_search = directory_input_menu.ask_user_for_input()
		
		file_searcher = FileSearcher(
			menu_option,
			items_to_search_for,
			directory_to_search
		)