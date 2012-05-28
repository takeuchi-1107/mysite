# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin

class FacePhoto(models.Model):
    name = models.CharField(max_length=200,unique=True)
    image = models.ImageField("写真", upload_to='photos')

class FacePhotoAdmin(admin.ModelAdmin):
    pass

#admin.site.register(FacePhoto, FacePhotoAdmin)