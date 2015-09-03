from whoosh.qparser import QueryParser
from whoosh import index
from whoosh import scoring
from whoosh.lang.porter import stem
BASEDIR = "/home/shubham/Dropbox/Library/7th_sem_lab/ir/Search_Engine/scripts/"

def operate(L,op,R):
    ret = []
    if op=='&':
        ret = [val for val in L if val in R]
    if op=='|':
        ret = list(set(L + R))
    if op=='~':
        for text in L:
            flag = 0
            for tt in R:
                if tt==text:
                    flag = 1
            if flag==0:
                ret.append(text)
    return ret

def search(id, querystring,scoring_measure):
    id = index.open_dir(BASEDIR+"index")
    qp = QueryParser("content", schema=id.schema)
    q = qp.parse(unicode(querystring))

    l = []

    foo = scoring.Frequency()

    if scoring_measure=="TF_IDF":
        foo = scoring.TF_IDF()
    if scoring_measure=="BM_25":
        foo = scoring.BM25()
    if scoring_measure=="TF":
        foo = scoring.Frequency()

    with id.searcher(weighting=foo) as s:
        results = s.search(q)
        for res in results:
            #print res['path'], res.score
            l.append(res['path'])
    return l

def multiwordquery(id, querystring, scoring):
    #print "querystring length = " + str(len(querystring))
    #print querystring
    if len(querystring)==1:
        return search(id,querystring,scoring)

    else :
        left = querystring[0]
        op = querystring[1]
        rem = querystring[2:]
        left_list = search(id,left,scoring)
        right_list = multiwordquery(id,rem,scoring)
        ret_list = operate(left_list, op, right_list)
        return ret_list

def multiwordquery_driver(id,x):
    # x = stem(x)
    x = x.split(' ')
    id = index.open_dir(BASEDIR+"index")
    return multiwordquery(id,x,scoring.TF_IDF())

# def main():
    # id = index.open_dir(BASEDIR+"index")
    # while (1<2):
        # x = raw_input()
        # xx = x.split(' ')
        # return multiwordquery(id,x,scoring.TF_IDF()) 
        # print "TF IDF LIST "
        # print multiwordquery_driver(id,x)

        # print "TF LIST"
        # data = search(id,xx,"TF")
        # for link in data:
            # print link

        # '''print "BM25 LIST"
        # print multiwordquery(id,xx,scoring.BM25F(B=0.75, content_B=1.0, K1=1.5))
        # '''
# main()
