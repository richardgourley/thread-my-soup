import os
from threading import Thread, Lock
from classes.directoryvalidation import DirectoryValidation
from classes.elementfinder import ElementFinder
from classes.fileretriever import FileRetriever
from classes.resultfilesetup import ResultFileSetUp
from classes.filehandler import FileHandler

element_finder = ElementFinder()

menu_options = [
        {
            'option_number':1,
            'option_name':'Search By Words - Find html elements with text containing words.',
            'enter_input_message':"Enter a word to search in the text. Press 'Q' or 'q' to stop entering words.",
            'blank_input_message':"The word you enter cannot be blank.",
            'search_function':element_finder.find_words
        },
        {
            'option_number':2,
            'option_name':'Search By Id or Class - Find html elements by id or class names.',
            'enter_input_message':"Enter a class or id to search for. Press 'Q' or 'q' to stop entering ids or classes.",
            'blank_input_message':"The class or id name you enter cannot be blank.",
            'search_function':element_finder.find_ids_or_classes
        },
        {
            'option_number':3,
            'option_name':'Search By HTML elements- Find specific html elements by name.',
            'enter_input_message':"Enter an html tag to search for. Press 'Q' or 'q' to stop entering html elements.",
            'blank_input_message':"The html tag name you enter cannot be blank.",
            'search_function':element_finder.find_html_elements
        }
    ]

'''
### CHOOSE OPTION NUMBER FROM menu_options
'''

has_chosen_option_number = False

while has_chosen_option_number == False:
    print("Choose an option:")
    for option in menu_options:
        print(option["option_number"], option["option_name"])

    option_number = input()

    if option_number == "":
        print("Choice cannot be blank.")
        continue
    elif option_number.isnumeric() == False:
        print("Please only enter a number")
        continue
    elif int(option_number) not in range(1,(len(menu_options) + 1)):
        print(f"Number must be between 1 and {len(menu_options)}.")
        continue
    else:
        print("You have chosen option number", option_number)
        has_chosen_option_number = True

'''
### INPUT WORDS, HTML TAGS, OR CLASSES AND IDS TO FIND WITHIN HTML FILES
'''

# Get the dictionary from menu_options based on the option_number chosen above
menu_option = menu_options[int(option_number) - 1]

print("============")
print("START ENTERING ITEMS TO FIND:")

items_to_search = []

still_entering_items = True

while still_entering_items:
    print(menu_option["enter_input_message"])
    item_input = input()

    if item_input == "":
        print(menu_option["blank_input_message"])
        continue

    if item_input == 'Q' or item_input == 'q':
        still_entering_items = False
        continue

    items_to_search.append(item_input)


'''
### ENTER A DIRECTORY OF HTML FILES TO SEARCH!
'''

print("==================")
print("ENTER A DIRECTORY TO SEARCH")
print("We will search for any HTML files.")
print("We will search through all sub directories.")
print('-------------------')
print("Please enter the full directory address, starting from your system root starting with a slash")
print("EXAMPLE: /home/user/webprojects/portfoliosite")

directory_to_search = ""
still_entering_directory = True

while still_entering_directory:
    directory_to_search = input()

    if directory_to_search == "":
        print("Directory name must not be blank")
        continue

    still_entering_directory = False


'''
### VALIDATE IF THE DIRECTORY EXISTS OR QUIT
'''

directory_validation = DirectoryValidation()

if directory_validation.validate_directory(directory_to_search) == False:
    print("Sorry the directory you entered does not exist. Please check and try again.")
    quit()

'''
## RETRIEVE FILES FROM THE DIRECTORY
'''

file_retriever = FileRetriever()
retrieved_files = file_retriever.retrieve_files_from_dir(directory_to_search)

if retrieved_files is None:
    print(f"We couldn't find the directory named {directory_to_search}. Please try again.")
    quit()

if len(retrieved_files) == 0:
    print(f"We could't find any html files in the {directory_to_search} directory.")
    print("Please check html files are in the directory and try again.")
    quit()
'''
## CREATE RESULTS DIR AND TIMESTAMPED RESULTS FILE
'''

result_file_setup = ResultFileSetUp()

if result_file_setup.check_results_dir_exists() == False:
    result_file_setup.make_results_dir()

timestamped_results_file = result_file_setup.create_timestamped_results_file()

'''
### FUNCTION TO PASS TO EACH THREAD TO RUN EACH FILE
'''

## File handler has parse_file and append_to_results_file methods
file_handler = FileHandler()

lock = Lock()

def retrieve_html_and_append_to_results_file(file):
    lock.acquire()

    soup = file_handler.parse_file(file)

    if soup is None:
        lock.release()
        return

    result_lists = menu_option["search_function"](soup, items_to_search)

    if result_lists is None:
        lock.release()
        return

    file_handler.append_to_results_file(result_lists, file, timestamped_results_file)

    lock.release()

'''
## START THREADS
'''

threads = [Thread(target=retrieve_html_and_append_to_results_file, args=(file,)) for file in retrieved_files]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

## END MESSAGE
print(f"Finished. You can find the results at '{timestamped_results_file}'.")








