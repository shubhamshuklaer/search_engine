# coding: utf8
# try something like
import math
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..","scripts")))
# from searcher import *
import searcher
# To prevent using older version of module because of caching
reload(searcher)
def index():
    tabs=[
            {"name":"TF","id":"tf"},
            {"name":"TF-IDF","id":"tf_idf"},
            {"name":"BM25","id":"bm_25"},
            ]
    return dict(tabs=tabs)

def get_results():
    if(request.vars["nlp_switch"]=="true"):
        return str(searcher.search(None,request.vars["search_bar"],request.vars["type"].upper()))
    else:
        return str(searcher.multiwordquery_driver(None,request.vars["search_bar"],request.vars["type"].upper()))


def build_paginator():
    paginator=""
    num_results=11
    num_pages=int(math.ceil(num_results/10.0))
    for i in range(num_pages):
        if(i==0):
            class_name="active";
        else:
            class_name="";
        paginator+=str(LI(A(i+1,_href="#"),_class=class_name))
    return paginator


