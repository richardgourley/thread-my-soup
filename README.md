# Thread My Soup

## INTRO
This is a handy tool to find and check html tag elements in your website pages quickly.  

Let's say you had some pages in your website where some headings were h4 and some were h5 in 15 of your site pages.  
You could enter h4 and h5 in the command line (see below) and then enter the urls you want to search. A results file would be created showing you all h4 and h5 tags from all 15 pages. 

Or imagine that you were using Bootstrap or Tailwind and you wanted to quickly check all paragraphs were using a class such as 'text-secondary'. You could get all of the paragraphs from many of your website pages in one file to check.

The idea of the tool is its quicker to get all elements that manually go through each website page.

## FEATURES
### Menu
- The user navigates to the directory containing the main file - 'threadmysoup.py'
- The user can enter ANY number of html tags - h1,h2,p,a,link,style etc. - that they would like to check.
- The user is then prompted to enter as many urls as they like from their websites that they would like to check.

### Search
- The search utilizes threading to search multiple urls
- The search uses the requests and BeautifulSoup libraries.

### Results File
- Rather than getting text from each element found, the results file displays all paragraphs, headings, links, titles, meta tags etc. as they are with a space inbetween.
- There is a ===END OF URL=== marking to separate url results.

## SCREENSHOTS

### Menu Page

![menupage](https://github.com/richardgourley/thread-my-soup/blob/main/screenshots/threadmysoupmenu.png)

### Results Page

![resultspage](https://github.com/richardgourley/thread-my-soup/blob/main/screenshots/threadmysoupresults.png)

## GETTING STARTED
Navigate to the main directory 'thread-my-soup'.

The program is started by entering the main program file and any number of html tags that you want to find in your website pages, separated by a space.
```
python3 threadmysoup.py p
python3 threadmysoup.py h1 p a
python3 threadmysoup.py link meta title p h4
python3 threadmysoup.py li section
```
The program then prompts you to enter as many of your website urls you would like to check for the elements entered in the command line.

A temp file is created using 'requests' to store the source code of each url. The temp file is then converted to a BeautifulSoup class, and the html tags you want to search are then found and appended to a file called 'results.txt' in the same folder.

