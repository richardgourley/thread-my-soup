from classes.htmltagargs import HtmlTagArgs
from classes.urlinputs import UrlInputs
from classes.htmltagsearcher import HtmlTagSearcher

if __name__ == "__main__":
	html_tag_args = HtmlTagArgs()

	html_tags = html_tag_args.return_html_tag_args()

	url_inputs = UrlInputs()

	urls = url_inputs.ask_user_for_inputs()
	
	## pass html_tag_args, urls and file names to html_tag_searcher to run program
	html_tag_searcher = HtmlTagSearcher(html_tags, urls, "temp.txt", "results.txt")



	 

	
