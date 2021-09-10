# Thread My Soup

## INTRO
This handy tool lets users search for and retrieve words or phrases, classes or ids and any html elements from any number of html files, using the Beautiful Soup and Threading modules.

Imagine you wanted to traverse through the directory storing all of your web development projects checking a specific html element, checking the spelling of a word, such as an address or customer name, or even inspecting elements with a specific id or class name. This program helps you to find specific elements from a large number of files by traversing large directories on your system.

All results are saved into the results directory in a timestamped results file.

## FEATURES
### Menu
- Args - the first menu allows the user to run the program with args to search words, search for classes or ids or search for specific html tags or elements.
- The second part of the menu asks the user to search through a directory called 'files' or the user can input any file on their system to traverse through every html file looking for the given elements.
- The final part of the menu asks the user to input the name of any directory on their system that they wish to search through to find elements. 

### Base classes 
- The 'UserInputBase' class is inherited by the 'UserInput' class which is instantiated in the main 'threadmysoup.py' file, giving the user the menu options required to choose type of search and where to search.

### Helper classes
- Instances of the helper classes are all created and used by the 'FileSearcher' and 'Args' classes.
- Methods from the helper classes 'ElementFinder', 'ThreadStarter', 'CommandLineArgs' and 'File Handler' are used in multiple classes allowing for code re-use.

- The idea is to allow extension of the program by having loosely coupled relationships between classes.

### Extendable
The program can be extended to add a new menu option in the 'menu_options' dictionary in the 'thread_soup.py' file.
A new method can be added to the 'ElementFinder class'. (See below)

![mainmenupage](https://github.com/richardgourley/thread-my-soup/blob/main/screenshots/threadmysoupmainmenu.png)

- The preferences option in 'threadmysoup.py' could easily be extended to use the requests library and find and check elements from the users live websites.

### Search
- The search utilizes threading to search multiple urls at the same time.
- The search uses the BeautifulSoup library.

### Results File
- A time and date stamped results file is added to a 'results' directory after every search.
- There is a ==== END OF FILE/ file name ==== marking to separate results.

## SCREENSHOTS

### Menu Page

![menupage](https://github.com/richardgourley/thread-my-soup/blob/main/screenshots/threadmysoupmenu.png)

### Results Page

![resultspage](https://github.com/richardgourley/thread-my-soup/blob/main/screenshots/threadmysoupresults.png)

## GETTING STARTED
Navigate to the main directory 'thread-my-soup'. Enter the line below to see the initial menu options.

```
python3 threadmysoup.py 

You need to run'threadmysoup.py' + 1 of the following menu options
EXAMPLES:
threadmysoup.py searchwords (find any words in the text)
threadmysoup.py searchidsorclasses (find elements with specific ids or classes)
threadmysoup.py searchhtmltags (find all html tags)

```

## TESTING
To run the tests in the 'tests' directory, from the main directory where 'threadmysoup.py' lives, run:
```
python3 -m unittest
```


