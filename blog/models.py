# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

categories = (
    ('Training', 'Training'),
    ('Mindset', 'Mindset'),
    ('Nutrition', 'Nutrition'),
    ('General', 'General')
)


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=250)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0)
    category = models.CharField(max_length=9, choices=categories, default='General')
    image = models.ImageField(upload_to='blog_images', blank=True)

    def publish(self):
        self.date_published = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title



