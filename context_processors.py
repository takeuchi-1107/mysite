
# -*- encoding: utf-8 -*-

#--------- import ---------
from django.conf import settings
from common.static_value import GameText

def media(request):
    return {'MEDIA_URL': settings.MEDIA_URL}

#------------------------------------------------
# @brief : デフォルトコンテキスト
#------------------------------------------------
def contexts(request):
    return {
        'GameText' : GameText,
        }