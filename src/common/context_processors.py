
# -*- encoding: utf-8 -*-

#--------- import ---------
from django.conf import settings
from src.common.static_value import StaticValue

#------------------------------------------------
# @brief : デフォルトコンテキスト
#------------------------------------------------
def contexts(request):
    return {
        'request': request,
        'StaticValue' : StaticValue,
    }

#------------------------------------------------
# @brief : { MEDIA_URL }を使用
#------------------------------------------------
def media(request):
    return {
        'MEDIA_URL': settings.MEDIA_URL,
        }