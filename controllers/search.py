# coding: utf8
# try something like
import math
import sys
import os
# from whoosh import index
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..","scripts")))
# from searcher import *
import searcher
import subtext
# To prevent using older version of module because of caching
reload(searcher)
reload(subtext)
num_results_per_page=10
def index():
    tabs=[
            {"name":"TF","id":"tf"},
            {"name":"TF-IDF","id":"tf_idf"},
            {"name":"BM25","id":"bm_25"},
            ]
    return dict(tabs=tabs)

def get_results():
    results=get_results_from_searcher(request.vars["nlp_switch"],request.vars["search_bar"],request.vars["type"].upper())
    ret_html=""
    page_num=int(request.vars["page_no"])
    for i in range(len(results)):
        if i+1> (page_num-1)*num_results_per_page and i+1<=page_num*num_results_per_page:
            result=results[i]
            ret_html+=str(LI(A(os.path.basename(result["path"]),_href=URL('search','display_page')+"?path="+result["path"]), \
                    SPAN(result["score"],_class="badge"),_class="list-group-item"))

    return ret_html

def display_page():
    data=""
    with open (request.vars["path"], "r") as myfile:
        data=myfile.read().replace('\n', '')

    return data

def get_results_from_searcher(nlp_switch,search_bar,scoring_measure):
    index_id=None
    results=dict()
    if(nlp_switch=="true"):
        results= searcher.search(index_id,search_bar,scoring_measure)
    else:
        results= searcher.multiwordquery_driver(index_id,search_bar,scoring_measure)


    return results

def get_max_num_results(nlp_switch,search_bar):
    len1=len(get_results_from_searcher(nlp_switch,search_bar,"TF"))
    len2=len(get_results_from_searcher(nlp_switch,search_bar,"TF_IDF"))
    len3=len(get_results_from_searcher(nlp_switch,search_bar,"BM_25"))
    return max(len1,max(len2,len3))

def build_paginator():
    paginator=""
    num_results=get_max_num_results(request.vars["nlp_switch"],request.vars["search_bar"])
    num_pages=int(math.ceil(float(num_results)/num_results_per_page))
    for i in range(num_pages):
        if(i==0):
            class_name="active";
        else:
            class_name="";
        paginator+=str(LI(A(i+1,_href="#"),_class=class_name))
    return paginator


