
# -*- encoding: utf-8 -*-

#=====================================================
# @file  :
# @brief :
#=====================================================

#--------- import ---------
from django.db import models
from django.forms import ModelForm

#------------------------------------------------
# @class : Entry
# @brief :
#------------------------------------------------
class Entry(models.Model):

    userid  = models.IntegerField()

    title   = models.CharField(max_length = 100)
    body    = models.TextField(max_length = 1000)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/entries/detail/%i" % self.id

class EntryForm(ModelForm):

    class Meta:
        model = Entry