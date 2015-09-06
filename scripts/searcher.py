from whoosh.qparser import QueryParser
from whoosh import index
from whoosh import scoring
from whoosh.lang.porter import stem
import os

BASEDIR = os.path.dirname(os.path.abspath(__file__))+"/"

# TODO change operate function to work with scores
def operate(L,op,R):
    ret = []
    if op=='&':
        for i in range(len(L)):
            for j in range(len(R)):
                if L[i]['path'] == R[j]['path']:
                    temp=dict()
                    temp["path"]=L[i]["path"]
                    temp["score"]=float(L[i]["score"]+R[j]["score"])/2
                    ret.append(temp)
                    break

    if op=='|':

        for i in range(len(L)):
            ret.append(L[i])


        for i in range(len(R)):
            xx = R[i]["path"]
            found = 0
            for j in range(len(ret)):
                if (ret[j]["path"]==xx):
                    found = 1
                    ret[j]["score"] = (ret[j]["score"] + R[i]["score"])/2.0

            if found==0:
                ret.append(R[i])


    if op=='~':
        for i in range(len(L)):
            found=0
            for j in range(len(R)):
                if L[i]['path'] == R[j]['path']:
                    found=1
                    break
            if found==0:
                temp=dict()
                temp["path"]=L[i]["path"]
                temp["score"]=L[i]["score"]
                ret.append(temp)
    return ret

# TODO check if BM25 is same as BM25F
def get_scoring(scoring_measure):
    foo = scoring.Frequency()

    if scoring_measure=="TF_IDF":
        foo = scoring.TF_IDF()
    if scoring_measure=="BM_25":
        foo = scoring.BM25F()
    if scoring_measure=="TF":
        foo = scoring.Frequency()
    return foo

def search(id, querystring,scoring_measure):
    # return BASEDIR
    id = index.open_dir(BASEDIR+"index")
    qp = QueryParser("content", schema=id.schema)
    q = qp.parse(unicode(querystring))

    l = []

    foo=get_scoring(scoring_measure)

    with id.searcher(weighting=foo) as s:
        results = s.search(q)
        for res in results:
            #print res['path'], res.score
            temp=dict()
            temp["path"]=res["path"]
            temp["score"]=res.score
            l.append(temp)
    return l



def multiwordquery(id, querystring, scoring_measure):
    #print "querystring length = " + str(len(querystring))
    #print querystring
    if len(querystring)==1:
        return search(id,querystring,scoring_measure)

    else :
        left = querystring[0]
        op = querystring[1]
        rem = querystring[2:]
        left_list = search(id,left,scoring_measure)
        right_list = multiwordquery(id,rem,scoring_measure)
        ret_list = operate(left_list, op, right_list)
        return ret_list

def multiwordquery_driver(id,x,scoring_measure):
    # x = stem(x)
    xx = x.split(' ')
    return multiwordquery(id,xx,scoring_measure)

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
