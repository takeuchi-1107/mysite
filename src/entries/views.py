# -*- coding: utf-8 -*-

#--------- import ---------
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from src.entries.models import Entry, EntryForm

#--------- template ---------
template_path = 'entries/'

def page_list( request, object_id ):

    list = None

    try:
        list = Entry.objects.filter(userid=request.user.id)
    except Entry.DoesNotExist:
        list = []


    ctxt = RequestContext( request, {'request': request, 'object_list': list} )

    return render_to_response( template_path + "entry_list.html", ctxt)


def create_entry( request ):

    if request.method == 'POST':
        new_data = request.POST.copy()
        new_data['userid'] = request.user.id

        form = EntryForm(new_data)

        if form.is_valid():
            obj = form.save()

            return HttpResponseRedirect( obj.get_absolute_url() )
    else:
        form = EntryForm()

    form = dict(form=form)

    ctxt = RequestContext( request, form )

    return render_to_response( template_path + 'entry_form.html', ctxt )



