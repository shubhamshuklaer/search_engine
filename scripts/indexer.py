import os.path
from os import walk
from whoosh import index
from whoosh.fields import Schema, ID, TEXT
from whoosh.qparser import QueryParser

templist = []
doclist = []

def build_doclist(mypath):
    for (dirpath, dirnames, filenames) in walk(mypath):
        templist.extend(filenames)
        break
    for filename in templist:
        fullpath = mypath + "/" + filename
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
    return Schema(path=ID(unique=True, stored=True), content=TEXT)


def add_doc(writer, path):
    fileobj = open(path, "rb")
    content = fileobj.read()
    fileobj.close()
    content = content.decode('UTF-8','ignore')
    writer.add_document(path=unicode(path), content=unicode(content))


def main():
    dirname = "/home/v_akshay/Desktop/index"
    #build dovument list
    build_doclist("/home/v_akshay/Desktop/db")
    print doclist
    build_index(dirname)
    print "thats it"

main()
