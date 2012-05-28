
# -*- coding: utf-8 -*-

# polls/urls.py
from django.conf.urls.defaults import *

#--------- path ---------
views_path = 'src.top.views'

#--------- top ---------
urlpatterns = patterns(views_path,
    # トップ
    (r'^$', 'index'),
    # 各ページへ遷移
    (r'^/(?P<jamp_page>)polls/$', 'jamp_index'),
    (r'^/(?P<jamp_page>)entries/$', 'jamp_index'),
)