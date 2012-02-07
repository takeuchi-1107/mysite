
# -*- coding: utf-8 -*-

# polls/urls.py
from django.conf.urls.defaults import *
#from top.models import Poll

# http://localhost:8000/top/

#
urlpatterns = patterns( 'mysite.top.views',
    (r'^$', 'index'),

    (r'^/(?P<jamp_name>)polls/$', 'jamp'),
    (r'^/(?P<jamp_name>)entries/$', 'jamp'),
)