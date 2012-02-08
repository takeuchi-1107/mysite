
# -*- encoding: utf-8 -*-

#=====================================================
# @file  :
# @breaf :
#=====================================================

#--------- import ---------
from django.db import models        #...
from django.contrib import admin    #...

import datetime

#------------------------------------------------
# @class :
# @breaf :
#------------------------------------------------
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # ...
    def __unicode__(self):
        return self.question

    # ...
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()

#------------------------------------------------
# @class :
# @breaf :
#------------------------------------------------
class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()

    # ...
    def __unicode__(self):
        return self.choice

#------------------------------------------------
# @class :
# @breaf :
#------------------------------------------------
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

#------------------------------------------------
# @breaf :
#------------------------------------------------
admin.site.register(Poll, PollAdmin)