# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from mypage.models import FacePhoto
from django.http import Http404
from django.views.generic.simple import direct_to_template
#------------------------------------------------
# @breaf : インデックス
#------------------------------------------------
def index(request):

    return render_to_response( 'mypage/index.html', { 'request': request } )

def homepage(request, username):
    if request.user.username!=username:
        raise Http404
    photoname = ''
    try:
        obj = FacePhoto.objects.get(name=username)
    except:
        pass
    else:
        photoname = obj.image.name
    #return render_to_response( 'mypage/homepage.html', { 'request': request, 'username':username, 'photoname':photoname } )
    return direct_to_template( request, 'mypage/homepage.html', { 'request': request, 'username':username, 'photoname':photoname })

def photo_upload(request):
    if request.method == "POST":
        post_data = request.POST
        post_data.update(request.FILES)

        image_file = post_data["image_file"]
        if image_file:
            username = request.user.username
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
            message = "アップロードを完了しました"
        else:
            message = "アップロードに失敗しました"
    else:
        message = "アップロードに失敗しました"

    return render_to_response('mypage/photo_upload.html', {'message': message}, context_instance=RequestContext(request))
