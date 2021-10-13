# Thread My Soup

## INTRO

- Handy tool allows you to find and inspect html elements from any directory on your system by utilizing the 'Threading' and 'BeautifulSoup' modules.
- You can find inspect html elements based on html element name, retrieve text from any html element based on a word or phrase, or find html elements by id or class names.

It can be handy for checking heading tags, finding contact details or inspecting the id or class used for large numbers of html pages you have in a directory.

All results are saved into the results directory in a timestamped results file.

## FEATURES
### Menu/ threadmysoup.py
- The first menu screen prompts the user to enter choose between searching for html elements, searching for words or phrases, or searching via ids or class names.
- The second part of the menu asks the user for a directory name to search in.

- The program checks if the directory exists or if there are any html files in the directory to search and informs the user.

- The program also 

### Classes - OOP
- The classes are called and instantiated in the main 'thread-my-soup' file.
- The classes are written following the 'Single' responsibility principle.

### Extendable
- The program is written to be extendable.
- The menu option dictionary can be updated with a new option added alongside a new method added to the 'ElementFinder' class.

![mainmenupage](https://github.com/richardgourley/thread-my-soup/blob/main/screenshots/threadmysoupmainmenu.png)

### Search
- The search utilizes threading to search multiple files at the same time.
- The search uses the BeautifulSoup library to retrieve html elements and text.

### Results File
- A time and date stamped results file is added to a 'results' directory after every search.
- There is a ==== END OF FILE/ file name ==== marking to separate results.

## SCREENSHOTS

### Menu Page

![menupage](https://github.com/richardgourley/thread-my-soup/blob/main/screenshots/threadmysoupmenu.png)

### Results Page

![resultspage](https://github.com/richardgourley/thread-my-soup/blob/main/screenshots/threadmysoupresults.png)

## GETTING STARTED
- It's easy to run. 
- Navigate to the main directory 'thread-my-soup'. Enter the line below to see the initial menu options.

```
python3 threadmysoup.py
```

## TESTING
- Navigate to the main directory 'thread-my-soup' and run:
```
python3 -m unittest
```


