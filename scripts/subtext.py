#To be modified
import urlparse
import urllib
import BeautifulSoup
from BeautifulSoup import BeautifulSoup
import re

def get_subtext(url,search_text):
    htmltext = urllib.urlopen(url).read()
    soup = BeautifulSoup(htmltext)
    [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
    visible_text = soup.getText()

    results = soup.body.findAll(text=re.compile(search_text))
    return results

    # for i in results:
        # print '\n'
        # print i
