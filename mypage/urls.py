
# -*- coding: utf-8 -*-

# polls/urls.py
from django.conf.urls.defaults import *

# http://localhost:8000/polls/

#
urlpatterns = patterns( 'mypage.views',
    # トップ
    (r'^$', 'index'),
)