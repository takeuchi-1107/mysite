
# -*- coding: utf-8 -*-

# polls/urls.py
from django.conf.urls.defaults import *
from mysite.polls.models import Poll

# http://localhost:8000/polls/

#
urlpatterns = patterns( 'polls.views',
    (r'^$', 'index'),
    (r'^(?P<object_id>\d+)/$', 'detail'),
    url(r'^(?P<object_id>\d+)/results/$', 'results', name='results'),
    (r'^(?P<object_id>\d+)/vote/$', 'vote'),
)