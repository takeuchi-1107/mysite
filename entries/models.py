
# -*- encoding: utf-8 -*-

#=====================================================
# @file  :
# @breaf :
#=====================================================

#--------- import ---------
from django.db import models

#------------------------------------------------
# @class : Entry
# @breaf :
#------------------------------------------------
class Entry(models.Model):

    title = models.CharField(max_length = 100)
    content = models.TextField(max_length = 1000)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/entries/detail/%i" % self.id