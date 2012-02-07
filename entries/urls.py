
## -*- coding: utf-8 -*-

#--------- import ---------
from django.conf.urls.defaults import *

#------------------------------------------------
# @breaf :
#------------------------------------------------
info_dict = {
    'queryset':Entry.objects.all(),
    }

#------------------------------------------------
# @breaf :
#------------------------------------------------
urlpatterns = patterns('',
    #
    ( r'^$', 'django.views.generic.list_detail.object_list', info_dict ),
    #
    ( r'^create/$', 'django.views.generic.create_update.create_object',
         {'model':Entry, 'post_save_redirect':'/entries/'} )
)