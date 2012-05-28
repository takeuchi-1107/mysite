
# -*- coding: utf-8 -*-

# polls/urls.py
from django.conf.urls.defaults import *

#--------- import ---------
views_path = 'src.polls.views'

#--------- polls ---------
urlpatterns = patterns( views_path,
    # トップ
#    (r'^$', 'index' ),
    # 詳細
#    (r'^(?P<object_id>\d+)/$', 'detail'),
    # 結果
#    url(r'^(?P<object_id>\d+)/results/$', 'results', name='results'),
    # 投票
#    (r'^(?P<object_id>\d+)/vote/$', 'vote'),
)