import os.path
from os import walk
from whoosh import index
from whoosh.fields import Schema, ID, TEXT
from whoosh.qparser import QueryParser
import BeautifulSoup
from BeautifulSoup import BeautifulSoup
from BeautifulSoup import Comment
import re

cnt = 0

BASEDIR = os.path.dirname(os.path.abspath(__file__))+"/"

templist = []
doclist = []

def beautify(text):
    soup = BeautifulSoup(text)

    comments = soup.findAll(text=lambda text:isinstance(text, Comment))
    [comment.extract() for comment in comments]

    [s.extract()
     for s in soup
     (['style', 'script', '[document]', 'head', 'title'])]
    all_text=soup.getText()
    return all_text

def build_doclist(mypath):
    for (dirpath, dirnames, filenames) in walk(mypath):
        templist.extend(filenames)
        break
    for filename in templist:
        fullpath = BASEDIR + "db/" + filename
        doclist.append(fullpath)

def build_index(dirname):
    # Always create the index from scratch
    ix = index.create_in(dirname, schema=get_schema())
    writer = ix.writer()

    # Assume we have a function that gathers the filenames of the
    # documents to be indexed
    for path in doclist:
        add_doc(writer, path)

    writer.commit()


def get_schema():
    return Schema(path=ID(unique=True, stored=True), content=TEXT(stored=True))


def add_doc(writer, path):
    #print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\n\n\n\n\n")
    global cnt
    print cnt+1
    cnt = cnt+1
    print(path)
    #print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\n\n\n\n\n")
    fileobj = open(path, "r")
    content = fileobj.read()
    fileobj.close()
    if len(content)==0:
        return
    #print content
    try:
        content = beautify(content)
        print "Scrapped ---------------------"
        #print content
        #content = content.decode('UTF-8','ignore')
        writer.add_document(path=unicode(path), content=unicode(content))
    except:
        return


def main():
    dirname = BASEDIR+"index/"
    #build dovument list
    build_doclist(BASEDIR+"db")
    #print doclist
    build_index(dirname)
    print "thats it"

main()
