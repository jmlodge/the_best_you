# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=250)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.date_published = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title



