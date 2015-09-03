# coding: utf8
# try something like
def index():
    search_form=FORM(INPUT(_type="text",_name="search_query",_placeholder="Search term", \
            _id="search_bar",_class="form-control",requires=IS_NOT_EMPTY()),_class="navbar-form \
        navbar-left")

    if search_form.process().accepted:
        search_query=search_form.vars.search_query
        response.flash=search_query

    tabs=[
            {"name":"TF","id":"tf"},
            {"name":"TF-IDF","id":"tf_idf"},
            {"name":"BM25","id":"b25"}
            ]
    return dict(search_form=search_form, tabs=tabs)

