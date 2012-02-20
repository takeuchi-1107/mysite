
# -*- encoding: utf-8 -*-

#=====================================================
# @file  :
# @brief :
#=====================================================

#--------- import ---------
from django.db import models        #...
from django.contrib import admin    #...

import datetime

#------------------------------------------------
# @class :
# @brief :
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
# @brief :
#------------------------------------------------
class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()

    # ...
    def __unicode__(self):
        return self.choice

class Vote(models.Model):
    choice = models.ForeignKey(Choice)
    username = models.CharField(max_length=200)

#------------------------------------------------
# @class :
# @brief :
#------------------------------------------------
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

class VoteAdmin(admin.ModelAdmin):
    list_display = ( 'username', 'test')
    def test(self, obj):
        o = Poll.objects.get(id=obj.choice.poll.id)
        return o.question
#------------------------------------------------
# @brief :
#------------------------------------------------
admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
admin.site.register(Vote, VoteAdmin)

