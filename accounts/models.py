# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # links UserProfile to an instance of accounts
    user = models.OneToOneField(User)
    # addition attributes
    website = models.URLField(blank=True)
    bio = models.TextField(max_length=400, blank=True)
    image = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username



