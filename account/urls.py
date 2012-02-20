
## -*- coding: utf-8 -*-

#=====================================================
# @file  : urls.py
# @brief : URLリンク定義
#=====================================================

#--------- import ---------
from django.conf.urls.defaults import *

#--------- URL ---------
urlpatterns = patterns('',
    #
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name':'./account/login.html'} ),
    #
    (r'^logout/$', 'django.contrib.auth.views.logout', {'template_name':'./account/logout.html'} ),
)
