
# -*- coding: utf-8 -*-

# polls/urls.py
from django.conf.urls.defaults import *


# http://localhost:8000/top/

#
urlpatterns = patterns( 'mysite.top.views',
    # トップ
    (r'^$', 'index'),
    # 各ページへ遷移
    (r'^/(?P<jamp_page>)polls/$', 'jamp_index'),
    (r'^/(?P<jamp_page>)entries/$', 'jamp_index'),
)