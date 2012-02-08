
## -*- coding: utf-8 -*-

#=====================================================
# @file  : urls.py
# @breaf : URLリンク定義
#=====================================================

#--------- import ---------
from django.conf.urls.defaults import *
from models import Entry

#--------- query ---------
info_dict = { 'queryset':Entry.objects.all(), }

#--------- URL ---------
urlpatterns = patterns('',
    # 一覧
    ( r'^$', 'django.views.generic.list_detail.object_list', info_dict ),
    # 新規作成
    ( r'^create/$', 'django.views.generic.create_update.create_object',
          {'model':Entry, 'post_save_redirect':'/entries/'} ),
    # 詳細閲覧
    ( r'^detail/(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict ),
    # 更新
    ( r'^update/(?P<object_id>\d+)/$', 'django.views.generic.create_update.update_object', {'model':Entry} ),
    # 削除
    ( r'^delete/(?P<object_id>\d+)/$', 'django.views.generic.create_update.delete_object',
         { 'model':Entry, 'post_delete_redirect':'/entries/' } ),
)