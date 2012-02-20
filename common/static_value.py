
# -*- encoding: utf-8 -*-

#------------------------------------------------
# @class : Entry
# @brief :
#------------------------------------------------
class StaticValue(object):

    array = [ "aaaaa", "<p>この項目を削除します。よろしいですか？</p><br/>", "あgfだgsdfvv"]

    def Test(self):
         print u'%s「お前の%sは俺の女だ！悔しかったら奪いに来い」！'  #array[0]
#
#<div id='page-title' class='page-title'>
#交換完了
#</div>
#<!--ﾍｯﾀﾞｰEND-->
#<div class="left">
#<span style="color:#E1AE00">所持{{SV.WORDS_MEDAL|h2z}}</span>:{{player.medal}}
#</div>
#    {% center_next %}
#
#<div class="left">
#舎弟{{shatei_num}}人を{{SV.WORDS_MEDAL|h2z}}{{medals}}枚と交換しました。
#</div>
#
#    {% center_next %}
#<div class="left">
#<a data-role="button" href="{% opensocial_url medal_charge_select %}">更に舎弟を{{SV.WORDS_MEDAL|h2z}}に交換</a>
#<a data-role="button" href="{% opensocial_url medal_exchange_list %}">スペシャルアイテムリストへ</a>