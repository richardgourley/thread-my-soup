from searchsetup import SearchSetUp
from elementretriever import ElementRetriever

def run(element_to_search):
	search_setup = SearchSetUp()

	urls = search_setup.ask_user_for_urls()

	element_retriever = ElementRetriever(urls, element_to_search)

	element_retriever.clear_file_content_from_previous()
	element_retriever.start_threads()

	print(f"The results can be found in the file: {element_retriever.results_file}")







