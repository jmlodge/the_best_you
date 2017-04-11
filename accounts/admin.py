# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from accounts.models import UserProfile


# registers new UserProfile Model with the admin interface
admin.site.register(UserProfile)

