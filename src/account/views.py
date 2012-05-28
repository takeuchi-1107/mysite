
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.db import IntegrityError

#--------- function ---------
def create( request ):

    try:
        name = request.POST['name']
        mail = ''#request.POST['mail']
        password = request.POST['pass']
        password2 = request.POST['pass2']

    except KeyError:
        return render_to_response('account/register.html', context_instance=RequestContext(request) )

    else:
        try:
            user = User.objects.create_user( name, mail, password)
        except IntegrityError:
            return render_to_response('account/register.html',
                                       {'message' : "指定のユーザは登録済みです。", 'success' : True, },
                                        context_instance=RequestContext(request) )
        except:
            return HttpResponseRedirect( '../register', )
        else:
            if password != password2:
                return render_to_response('account/register.html',
                        {'message' : "パスワードが一致しません。", 'success' : True, },
                        context_instance=RequestContext(request) )
            elif name == "" or name == None:
                return render_to_response('account/register.html',
                        {'message' : "ユーザー名を入力してください。", 'success' : True, },
                        context_instance=RequestContext(request) )

    return render_to_response('account/register.html',
            {'message' : "ユーザーを作成しました。", 'success' : False, },
            context_instance=RequestContext(request) )


def register( request, name, mail, password ):

    User.objects.create_user( name, mail, password)

    return HttpResponseRedirect("/top/")
