
# -*- coding: utf-8 -*-

#=====================================================
# @file  : view.py
# @brief : 投票機能定義
#=====================================================

#--------- import ---------
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from mysite.polls.models import Poll, Choice, Vote

#------------------------------------------------
# @brief : 初期
#------------------------------------------------
def index(request):
    object_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('polls/index.html', { 'object_list': object_list } )

#------------------------------------------------
# @brief : 詳細
#------------------------------------------------

#--------- import ---------
from django.shortcuts import render_to_response, get_object_or_404

#--------- function ---------
def detail( request, object_id ):
    p = get_object_or_404( Poll, pk=object_id )
    return render_to_response( 'polls/detail.html', {'object': p} )

#------------------------------------------------
# @brief : 投票
#------------------------------------------------

#--------- import ---------
import os
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from mysite.polls.models import Choice, Poll

#--------- function ---------
def vote(request, object_id):

    p = get_object_or_404( Poll, pk=object_id )

    #------ 投票対象を選択しているか ------
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])

    #------ 否選択 ------
    except (KeyError, Choice.DoesNotExist):
        # 投票フォームを再表示
        return render_to_response('polls/detail.html', {
            'object': p,
            'error_message' : "選択肢を選んでいません。",
            }, context_instance=RequestContext(request) )

    #------ 選択中 ------
    else:
        # 投票状況を更新
        selected_choice.votes += 1
        selected_choice.save()
        vote = Vote()
        vote.choice = selected_choice
        if request.user.is_anonymous():
            vote.username = 'anonymous'
        else:
            vote.username = request.user.username
        vote.save()
    #    selected_choice.vote_set.
        # ユーザが Back ボタンを押して同じフォームを提出するのを防ぐ
        # ため、POST データを処理できた場合には、必ずHttpResponseRedirect を返すようにします。
        return HttpResponseRedirect( reverse( 'results', args=(p.id,)))

#------------------------------------------------
# @brief : 結果
#------------------------------------------------
def results(request, object_id):
    p = get_object_or_404( Poll, pk=object_id )
    return render_to_response( 'polls/results.html', { 'object': p } )

# End of File