
# -*- encoding: utf-8 -*-

#=====================================================
# @file  :
# @breaf :
#=====================================================

#--------- import ---------
from django.shortcuts import render_to_response

#------------------------------------------------
# @breaf : 初期
#------------------------------------------------
def index(request):
    return render_to_response('top/index.html', request )

#------------------------------------------------
# @breaf :
#------------------------------------------------
def jamp(request):
    return render_to_response( jamp_name + '/index.html', request )

# End of File