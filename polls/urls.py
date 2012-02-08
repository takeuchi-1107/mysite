
# -*- coding: utf-8 -*-

# polls/urls.py
from django.conf.urls.defaults import *

# http://localhost:8000/polls/

#
urlpatterns = patterns( 'polls.views',
    # トップ
    (r'^$', 'index'),
    # 詳細
    (r'^(?P<object_id>\d+)/$', 'detail'),
    # 結果
    url(r'^(?P<object_id>\d+)/results/$', 'results', name='results'),
    # 投票
    (r'^(?P<object_id>\d+)/vote/$', 'vote'),
)