
## -*- coding: utf-8 -*-

#=====================================================
# @file  : urls.py
# @brief : URLリンク定義
#=====================================================

#--------- import ---------
from django.conf.urls.defaults import *

#--------- URL ---------
urlpatterns = patterns('',
    # 新規作成
    (r'^create/$', 'account.views.create', '' ),
    # 新規登録
    (r'^register/$', 'account.views.register', '' ),
    # ログイン
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name':'./account/login.html'} ),
    # ログアウト
    (r'^logout/$', 'django.contrib.auth.views.logout', {'template_name':'./account/logout.html'} ),
    # 認証終了後リダイレクト
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/entries/page/1/'}),
)
