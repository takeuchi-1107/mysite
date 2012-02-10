# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
#------------------------------------------------
# @breaf : インデックス
#------------------------------------------------
def index(request):
    return render_to_response( 'mypage/index.html')#, { 'object': p } )
