# coding: utf8
# try something like
import math
import sys
sys.path.append("/home/shubham/Dropbox/Library/7th_sem_lab/ir/Search_Engine/scripts")
from searcher import *
def index():
    search_form=FORM(INPUT(_type="text",_name="search_query",_placeholder="Search term", \
            _id="search_bar",_class="form-control",requires=IS_NOT_EMPTY()),LABEL("NLP Mode",_id="nlp_mode_label"),INPUT(_type="checkbox", \
            _name="nlp_checkbox",_id="nlp_switch",_checked=True),_class="navbar-form \
        navbar-left")

    if search_form.process().accepted:
        search_query=search_form.vars.search_query
        response.flash=search_query

    tabs=[
            {"name":"TF","id":"tf"},
            {"name":"TF-IDF","id":"tf_idf"},
            {"name":"BM25","id":"bm_25"},
            ]
    return dict(tabs=tabs)

def get_results():
    return str(multiwordquery_driver(None,"led"))
    if(request.vars["nlp_switch"]=="true"):
        return str(search(None,request.vars["search_bar"],request.vars["type"].upper()))
    else:
        return str(multiwordquery_driver(None,request.vars["search_bar"]))


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

