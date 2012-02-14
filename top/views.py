
# -*- encoding: utf-8 -*-

#=====================================================
# @file  : views.py
# @breaf : トップページview定義
#=====================================================

#--------- import ---------
from django.shortcuts import render_to_response


#------------------------------------------------
# @breaf : 初期ページ呼び出し
#------------------------------------------------
def index(request):
    b = request.user.is_anonymous()
#    if b == True:
    print b
    return render_to_response('top/index.html', {"request":request})

#------------------------------------------------
# @breaf : 各トップページへ遷移
#------------------------------------------------
def jamp_index(request):
    return render_to_response( jamp_page + '/index.html', request )

# End of File