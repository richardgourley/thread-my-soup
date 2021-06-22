# Thread My Soup
A tool that utilizes sys.argsv, the requests library, threading and Beautiful Soup to retrieve elements from one of your live web pages. 

It can be used to retrieve and check text and links are working from your own website pages, for these elements: 

a, h1, h2, h3, h4, h5, p, ul, li, span or title.

You can retrieve elements from any number of url pages you like every time the program is run.

## Getting started
Navigate to the main directory 'thread-my-soup'.

The program is called using an argument of the element you want to retrieve entered after the file name eg.
```
python3 threadmysoup.py p
python3 threadmysoup.py h1
python3 threadmysoup.py a
python3 threadmysoup.py li
```

The file 'tests.py' imports unittest and makes assertions on classes and methods. If you extend the program to suit your needs you can modify or extend the 'tests.py' file to test new assertions.

Run tests by navigating the main project directory 'thread-my-soup' and running:
```
python3 tests.py
```

## Tools Used
- requests
- threading
- bs4 - BeautifulSoup
- sys.argsv used - command line arguments added
- threading - a thread started for each url
- lock - acquire and release
- context managers - with open(file) as f... 

## Feautures
- Uses threading to visit urls concurrently. Should be more performant than single threaded programs.
- Url content for each url saved in 'temp.txt', then elements retrieved and saved in 'results.txt'.
- Uses a command line argument of the element you want to search.

- Adaptable -> modify the program if you want to adapt it to include more complex arguments for BeautifulSoup such as finding all elements that match a class name or an id.

