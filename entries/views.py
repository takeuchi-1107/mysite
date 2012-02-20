# -*- coding: utf-8 -*-

#--------- import ---------
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Entry

from django.views.generic.simple import direct_to_template

#------------------------------------------------
# @brief : インデックス
#------------------------------------------------
def entries_list(request):

    ctxt = RequestContext(request, { 'object_list':Entry.objects.all(), } )

    return render_to_response( 'entries/entry_list.html', ctxt )
    #return direct_to_template( 'entries/entry_list.html', ctxt )