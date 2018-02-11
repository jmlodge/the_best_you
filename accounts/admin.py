# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import User

# registers new UserProfile Model with the admin interface

admin.site.register(User)
