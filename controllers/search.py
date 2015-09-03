# coding: utf8
# try something like
import math
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
            {"name":"BM25","id":"b25"},
            ]
    return dict(tabs=tabs)

def get_results():
    return request.vars["type"]+" "+request.vars["page_no"]+" "+request.vars["search_bar"]+" "+request.vars["nlp_switch"]

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

