# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from accounts.forms import UserForm, UserProfileForm
from django.contrib import messages


def register(request):
    # boolean set to false as user not yet registered set to true upon completion
    registered = False

    if request.method == 'POST':
        # if 'post' attempt to get data from raw form input
        user_form = UserForm(data=request.POST)
        user_profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and user_profile_form.is_valid():
            # save user data to DB
            user = user_form.save()
            # hash password with set_password
            user.set_password(user.password)
            user.save()

            profile = user_profile_form.save(commit=False)
            profile.user = user

            if 'image' in request.FILES:
                profile.image = request.FILES['image']

            profile.save()
            registered = True

        else:
            print(user_form.errors, user_profile_form.errors)

    else:
        user_form = UserForm
        user_profile_form = UserProfileForm

    return render(request,
                  'accounts/register.html',
                  {'user_form': user_form, 'user_profile_form': user_profile_form,'registered': registered})
