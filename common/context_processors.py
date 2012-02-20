
# -*- encoding: utf-8 -*-

#--------- import ---------
from common.static_value import StaticValue
from common.game_text import GameText

#------------------------------------------------
# @brief : デフォルトコンテキスト
#------------------------------------------------
def contexts(request):
    return {
        'StaticValue' : StaticValue,
        'GameText' : GameText,
    }