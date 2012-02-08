
# -*- encoding: utf-8 -*-

#=====================================================
# @file  : urls.py
# @breaf : URLリンク定義
#=====================================================

#--------- import ---------
from django.conf.urls.defaults import *

#--------- URL ---------
urlpatterns = patterns('',
    # top
    ( r'^top/', include('top.urls') ),
    # polls
    ( r'^polls/', include('polls.urls') ),
    # entries
    (r'^entries/', include('entries.urls')),
)

