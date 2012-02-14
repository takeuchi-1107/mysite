
# -*- encoding: utf-8 -*-
from django.conf import settings
def media(request):
    return {'MEDIA_URL': settings.MEDIA_URL}
