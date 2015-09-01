from whoosh.qparser import QueryParser
from whoosh import index
from whoosh import scoring

def search(id, querystring,scoring):
    qp = QueryParser("content", schema=id.schema)
    q = qp.parse(unicode(querystring))

    with id.searcher(weighting=scoring) as s:
        results = s.search(q)
        for res in results:
            print res['path'], res.score

def main():
    id = index.open_dir("/home/v_akshay/Desktop/index")
    while (1<2):
        x = raw_input()
        print "TF IDF LIST "
        search(id,x,scoring.TF_IDF())

        print "TF LIST"
        search(id,x,scoring.Frequency())

        print "BM25 LIST"
        search(id,x,scoring.BM25F(B=0.75, content_B=1.0, K1=1.5))
main()
