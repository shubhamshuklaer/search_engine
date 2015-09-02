# coding: utf8
# try something like
def index():
    form=SQLFORM.factory(Field('search_query', label='', requires=IS_NOT_EMPTY()),buttons=[])
    if form.process().accepted:
        search_query=form.vars.search_query
        response.flash=search_query
    return dict(form=form)

