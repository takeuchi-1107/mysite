
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
    # admin : http://127.0.0.1:8000/admin/
    ( r'^admin/', include( admin.site.urls ) ),
)

#--------- URL ---------
urlpatterns += patterns('',
    (r'^medias/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    # top : http://127.0.0.1:8000/top/
    ( r'^top/', include('top.urls') ),
    # polls : http://127.0.0.1:8000/polls/
    ( r'^polls/', include('polls.urls') ),
    # entries : http://127.0.0.1:8000/entries/
    ( r'^entries/', include('entries.urls') ),
    # account : http://127.0.0.1:8000/account/
    ( r'^account/', include('account.urls') ),
    # mypage : http://127.0.0.1:8000/mypage/
    ( r'^mypage/', include('mypage.urls') ),
)

#--------- CSS ---------
if settings.DEBUG:
    urlpatterns += patterns('',
        ( r'^static/(?P<path>.*)', 'django.views.static.serve',
             {'document_root' : os.path.dirname(__file__) + '/static'} ),
    )
