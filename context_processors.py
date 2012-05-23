
# -*- encoding: utf-8 -*-

#--------- import ---------
from django.conf import settings

def media(request):
    return {'MEDIA_URL': settings.MEDIA_URL}