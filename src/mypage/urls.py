
# -*- coding: utf-8 -*-

# polls/urls.py
from django.conf.urls.defaults import *

#--------- path ---------
views_path = 'src.mypage.views'

#
urlpatterns = patterns( views_path,
    # トップ
    (r'^$', 'index'),
    (r'^home/(?P<username>.+)/$', 'homepage'),
    (r'^photo_upload/$', 'photo_upload'),
    url( r'^result/(?P<username>.+)/(?P<resu>.+)/$', 'result', name='result'),
)