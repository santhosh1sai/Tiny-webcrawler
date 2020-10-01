#install beautifulSoap for the crawler to work
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#Be careful while using this crawler in ssl websites, some debugging will be needed

#import the libraries
import urllib.request,urllib.error,urllib.parse
from bs4 import BeautifulSoup

#Take the input
url = input('Enter - ')

#opening the url and reading the html
html = urllib.request.urlopen(url).read()

#paring the html
soup = BeautifulSoup(html, 'html.parser')

#targeting the a tags
tags = soup('a')

#for loop for iteration, and using the get command which acts as a dictionary
for tag in tags:
    print(tag.get('href', None))
