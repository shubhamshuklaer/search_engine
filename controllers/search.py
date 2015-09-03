# coding: utf8
# try something like
def index():
    search_form=FORM(INPUT(_type="text",_name="search_query",_placeholder="Search term", \
            _id="search_bar",_class="form-control",requires=IS_NOT_EMPTY()),LABEL("NLP Mode",_id="nlp_mode_label"),INPUT(_type="checkbox", \
            _name="nlp_checkbox",_id="nlp_switch",_checked=True),_class="navbar-form \
        navbar-left")

    if search_form.process().accepted:
        search_query=search_form.vars.search_query
        response.flash=search_query

    tabs=[
            {"name":"TF","id":"tf","items":[{"href":"fasdfas"},{"href":"adsfasdfsd"},{"href":"aaaaaa"}]},
            {"name":"TF-IDF","id":"tf_idf","items":[{"href":"fasdfas"},{"href":"adsfasdfsd"},{"href":"aaaraa"}]},
            {"name":"BM25","id":"b25","items":[{"href":"fasdfas"},{"href":"adsfasdfsd"},{"href":"aaaaad"}]}
            ]
    return dict(search_form=search_form, tabs=tabs,num_results=11)

def get_results():
    return request.vars["type"]+" "+request.vars["page_no"]

