
# -*- encoding: utf-8 -*-

#=====================================================
# @file  : urls.py
# @brief : URLリンク定義
#=====================================================

#--------- import ---------
from django.contrib import admin

from entries.models import Entry

#------------------------------------------------
# @brief : 登録
#------------------------------------------------
admin.site.register( Entry )