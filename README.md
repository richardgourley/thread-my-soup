# Thread My Soup

## INTRO
This handy tool lets users retrieve any html tags or elements from any number of their web pages into one easy to browse file.

Imagine if you needed to check all h1, p, link or ul tags across numerous pages. Doing this manually would take time.  This tool allows you to target specific tags and elements from multiple pages on your websites and inspect them from one file, with a divider between urls.

## FEATURES
### Adaptable
### Base classes
- The main classes are called in the 'threadmysoup.py'
- The main classes all inherit from one or more base classes.
- The program can be changed by editing the main classes but keeping the base classes as they are.
- The program could be adapted to check html files in a dir instead of your live websites.
- The program could be changed to check ids or classes instead of html tags.

### Menu
- The user can enter ANY number of html tags and elements - h1,h2,p,a,ul,link,style etc.
- The user can enter as many urls as they like from their websites that they would like to view how the html tags look.

### Search
- The search utilizes threading to search multiple urls at the same time.
- The search uses the requests and BeautifulSoup libraries.

### Results File
- The results file displays all requested html tags with all ids and classes displayed.
- There is a ===END OF URL=== marking to separate url results.

## SCREENSHOTS

### Menu Page

![menupage](https://github.com/richardgourley/thread-my-soup/blob/main/screenshots/threadmysoupmenu.png)

### Results Page

![resultspage](https://github.com/richardgourley/thread-my-soup/blob/main/screenshots/threadmysoupresults.png)

## GETTING STARTED
Navigate to the main directory 'thread-my-soup'.

The program is started by entering the main program file and any number of html tags:
```
python3 threadmysoup.py p
python3 threadmysoup.py h1 p a
python3 threadmysoup.py link meta title p h4
python3 threadmysoup.py li section
```
The program then prompts you to enter as many of your website urls as you would like to search.

A temp file is created for each url before all requested html tags and elements appear in a 'results.txt' file.

## TESTING
To run the tests in the 'tests' directory, from the main directory where 'threadmysoup.py' lives, run:
```
python3 -m unittest
```


