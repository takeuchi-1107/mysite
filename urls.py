
# -*- encoding: utf-8 -*-

#=====================================================
# @file  : urls.py
# @breaf : URLリンク定義
#=====================================================

#--------- import ---------
from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

import os

#--------- admin ---------
admin.autodiscover() # 管理画面のため

urlpatterns = patterns('',
    ( r'^admin/', include( admin.site.urls ) ),
)

#--------- URL ---------
urlpatterns += patterns('',
    # top
    ( r'^top/', include('top.urls') ),
    # polls
    ( r'^polls/', include('polls.urls') ),
    # entries
    ( r'^entries/', include('entries.urls') ),
    # account
    ( r'^account/', include('account.urls') ),
)

#--------- CSS ---------
if settings.DEBUG:
    urlpatterns += patterns('',
        ( r'^static/(?P<path>.*)', 'django.views.static.serve',
             {'document_root' : os.path.dirname(__file__) + '/static'} ),
    )
