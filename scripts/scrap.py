#All modified
import urlparse
import urllib
import BeautifulSoup
from BeautifulSoup import BeautifulSoup
from BeautifulSoup import Comment
import re

url = "index.html"


htmltext = urllib.urlopen(url).read()
soup = BeautifulSoup(htmltext)
texts = soup.findAll(text=True)


comments = soup.findAll(text=lambda text:isinstance(text, Comment))
#print comments
[comment.extract() for comment in comments]

[s.extract()
 for s in soup
 (['style', 'script', '[document]', 'head', 'title'])]
all_text=soup.getText()

print all_text
