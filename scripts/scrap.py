#To be modified
import urlparse
import urllib
import BeautifulSoup
from BeautifulSoup import BeautifulSoup

url = "index.html"


htmltext = urllib.urlopen(url).read()
soup = BeautifulSoup(htmltext)
texts = soup.findAll(text=True)

soup = BeautifulSoup(htmltext)
[s.extract()
 for s in soup
 (['style', 'script', '[document]', 'head', 'title'])]
all_text=soup.getText()
print all_text
