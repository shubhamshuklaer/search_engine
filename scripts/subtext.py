#To be modified
import urlparse
import urllib
import BeautifulSoup
from BeautifulSoup import BeautifulSoup
import re

url = "index.html"


htmltext = urllib.urlopen(url).read()

soup = BeautifulSoup(htmltext)
[s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
visible_text = soup.getText()
#print visible_text

results = soup.body.findAll(text=re.compile('tools'))

for i in results:
    print '\n'
    print i
