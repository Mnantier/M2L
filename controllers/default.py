# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    """
    Page d'accueil
    """
    message = "Bienvenue sur le portail de la Maison des Ligues !"
    return locals()


def statutJuridique():
    """
    Page statut juridique
    """
    return locals()


def aggregatorVosges():
    import gluon.contrib.feedparser as feedparser
    d = feedparser.parse(
        "http://www.vosgesmatin.fr/sport/rss")
    return dict(title=d.channel.title,
                link = d.channel.link,
                description = d.channel.description,
                created_on = request.now,
                entries = [
                  dict(title = entry.title,
                  link = entry.link,
                  description = entry.description,
                  created_on = request.now) for entry in d.entries])

def espacePresse():
    import gluon.contrib.feedparser as feedparser
    rssVosges = aggregatorVosges()
    return locals()

def servicePropose():
    """
    Page des services
    """
    return locals()

def nosLocaux():
    """
    Page de structuration des locaux
    """
    return locals()

def parcInformatique():
    """
    Page  du parc informatique
    """
    return locals()

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
