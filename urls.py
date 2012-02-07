
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # top
    ( r'^top/', include('top.urls') ),
    # polls
    ( r'^polls/', include('polls.urls') ),
    # entries
    (r'^entries/', include('entries.urls')),
)

