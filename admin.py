
# -*- encoding: utf-8 -*-

#=====================================================
# @file  : urls.py
# @breaf : URLリンク定義
#=====================================================

#--------- import ---------
from django.contrib import admin

from entries.models import Entry

#------------------------------------------------
# @breaf : 登録
#------------------------------------------------
admin.site.register(Entry)