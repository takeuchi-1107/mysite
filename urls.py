

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^polls/', include('mysite.polls.urls')),
)

