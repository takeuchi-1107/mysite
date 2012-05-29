# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from src.mypage.models import FacePhoto
from django.http import Http404, HttpResponseRedirect
from django.views.generic.simple import direct_to_template

#------------------------------------------------
# @brief : インデックス
#------------------------------------------------
def index(request):
    return render_to_response( 'mypage/index.html', { 'request': request } )

def homepage(request, username):
    account = User.objects.get(username=username)
    if not account:
        raise Http404
    photoname = ''
    try:
        obj = FacePhoto.objects.get(name=username)
    except:
        pass
    else:
        photoname = obj.image.name

    return direct_to_template( request, 'mypage/homepage.html', { 'request': request, 'username':username, 'photoname':photoname })

#
def result_entrypage(request):

    ctxt = RequestContext( request, {'message': message,'username':username} )

    return render_to_response('mypage/photo_upload.html', ctxt )

def photo_upload(request):
    username = request.user.username
    if request.method == "POST":
        post_data = request.POST
        post_data.update(request.FILES)

        image_file = post_data["image_file"]
        if image_file:
            # すでにあれば削除
            try:
                obj = FacePhoto.objects.get(name=username)
            except:
                pass
            else:
                obj.delete()
            filename = image_file._name#["filename"]
            photo = FacePhoto()
            photo.name = username
            photo.image = filename
            photo.image.save(filename, image_file)#["content"])
            photo.save()
            return HttpResponseRedirect(reverse('result', kwargs=dict({'username':username,'resu':1})),)
        else:
            return HttpResponseRedirect(reverse('result', kwargs=dict({'username':username,'resu':0})),)
    else:
        message = ""

    ctxt = RequestContext( request, {'message': message,'username':username} )

    return render_to_response('mypage/photo_upload.html', ctxt )

#
def result(request, username, resu):

    ctxt = RequestContext( request, { 'username':username,'resu':resu} )

    return render_to_response('mypage/result.html', ctxt )