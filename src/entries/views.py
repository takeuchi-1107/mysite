# -*- coding: utf-8 -*-

#--------- import ---------
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from src.entries.models import Entry, EntryForm

#--------- template ---------
template_path = 'entries/'

def page_list( request, object_id ):

    list = None

    try:
        list = Entry.objects.filter(userid=request.user.id)
    except Entry.DoesNotExist:
        list = []

    return render_to_response( template_path + "entry_list.html", {'request': request, 'object_list': list});


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

    return render_to_response( template_path + 'entry_form.html', form )



