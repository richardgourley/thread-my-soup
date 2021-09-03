# Thread My Soup

## INTRO
This handy tool lets users search for words or phrases, class or ids and search for and retrieve any html element in urls from their live websites or from any number of html files, using the requests, Beautiful Soup and Threading modules.

All results are saved into the results directory in a timestamped results file.

## FEATURES
### Menu
- Args - the first menu allows the user to run the program with args to search words, search for classes or ids or search for specific html tags or elements.
- The second part of the menu asks the user to enter inputs to search for, based upon their choice from the main args menu above.
- The final part of the menu asks the user to search through files or urls and then either prompts the user to ensure they have files in the 'files' dir or prompts the user to enter mutiple urls to search through.

### Base classes (inheritance)
- The 'MainInputsMenu' and 'UrlInputsMenu' classes inherit from the 'UrlInputBase' class.

### Helper classes (composition)
- Instances of the helper classes are all created and used by the 'FileSearcher', 'UrlSearcher' and 'Args' classes.
- Methods from the helper classes 'ElementFinder', 'ThreadStarter', 'CommandLineArgs' and 'UrlHandler' are used in multiple classes allowing for code re-use.

- The idea is to allow extension of the program by having loosely coupled relationships between classes.

### Extendable
The program can be extended to add a new menu option and a search html method added by extending:
- Args
  - A new args menu option can be added to the 'menu_options' dictionary

- ElementFinder 
  - A new method can be added to retrieve any type of filtered results from an html page or file.

- MainInputsMenu
  - The new menu option can be added to the init method.
  - The new menu option can be updated in the 'get_result_lists_based_on_menu_option' method.

### Search
- The search utilizes threading to search multiple urls at the same time.
- The search uses the requests and BeautifulSoup libraries.

### Results File
- A time and date stamped results file is added to a 'results' directory after every search.
- There is a ===END OF URL=== or a ==== END OF FILE==== marking to separate results from each url or file.

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


