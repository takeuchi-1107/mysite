
# -*- coding: utf-8 -*-

#=====================================================
# @bref
#=====================================================

#--------- import ---------
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from mysite.polls.models import Poll

#------------------------------------------------
#
#------------------------------------------------

#--------- import ---------
from django.shortcuts import render_to_response, get_object_or_404

#...
def detail( request, object_id ):
    p = get_object_or_404( Poll, pk=object_id )
    return render_to_response( 'polls/detail.html', {'object': p} )

#------------------------------------------------
# @breaf: vote
#------------------------------------------------

#--------- import ---------
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from mysite.polls.models import Choice, Poll

#...
def vote(request, object_id):
    p = get_object_or_404(Poll, pk=object_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Poll 投票フォームを再表示
        return render_to_response('polls/poll_detail.html', {
            'object': p,
            'error_message' : "選択肢を選んでいません。",
            }, context_instance=RequestContext(request) )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # ユーザが Back ボタンを押して同じフォームを提出するのを防ぐ
        # ため、POST データを処理できた場合には、必ずHttpResponseRedirect を返すようにします。
        return HttpResponseRedirect( reverse( 'poll_results', args=(p.id,) ) )

#------------------------------------------------
# @breaf: results
#------------------------------------------------
def results(request, object_id):
    p = get_object_or_404(Poll, pk=object_id)
    return render_to_response('polls/results.html', {'poll': p})