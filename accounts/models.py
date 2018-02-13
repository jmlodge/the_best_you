# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, UserManager


class AccountUserManager(UserManager):
    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()

        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)

        user.save(using=self._db)

        return user


class User(AbstractUser):
    # now that we've abstracted this class we can add any
    # number of custom attribute to our user class
    # in later units we'll be adding things like payment details!

    stripe_id = models.CharField(max_length=50, default='')
    subscription_end = models.DateTimeField(default=timezone.now)
    objects = AccountUserManager()

    def __unicode__(self):
        return self.username






