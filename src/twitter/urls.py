
# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
#from django.conf.urls.defaults import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#--------- path ---------
views_path = 'src.twitter.views'

#--------- url ---------
urlpatterns = patterns( views_path,
    # Top Page
    url(r'^oauth/$', 'index', name='twitter-index'),
    # Twitter OAuth Authenticate
    url(r'^oauth/get/$', 'get', name='twitter-get'),
    # Callback
    url(r'^oauth/get_callback/$', 'get_callback', name='twitter-get_callback'),
    # Redirect Page of after Authenticate
    url(r'^oauth/oauth_index/$', 'oauth_index', name='twitter-oauth_index'),
    # Tweet
    url(r'^oauth/post/$', 'post', name='twitter-post'),
)