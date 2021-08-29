from classes.args import Args
from classes.iteminputs import ItemInputs
from classes.urlinputs import UrlInputs
from classes.filesearcher import FileSearcher
from classes.urlsearcher import UrlSearcher

if __name__ == "__main__":
	args = Args()
	return_args = args.return_args()
	menu_option = return_args[0]

	item_inputs = ItemInputs(menu_option)
	items_to_search_for = item_inputs.ask_user_for_inputs()

	search_urls_or_files = item_inputs.ask_user_for_preference(["files", "urls"], "Would you like to enter urls or search through html files?")

	if search_urls_or_files == "files":
		file_searcher = FileSearcher(
			menu_option,
			items_to_search_for
		)
	else:
		url_inputs = UrlInputs()
		urls_to_search = url_inputs.ask_user_for_inputs()
		url_searcher = UrlSearcher(
			menu_option,
			items_to_search_for,
			urls_to_search
		)
