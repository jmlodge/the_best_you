# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from accounts.models import User
from accounts.forms import UserRegistrationForm, UserLoginForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from django.conf import settings
import stripe
import arrow
import datetime

stripe.api_key = settings.STRIPE_SECRET


def register(request):

    if request.method == 'POST':
        # if 'post' attempt to get data from raw form input
        form = UserRegistrationForm(data=request.POST)

        if form.is_valid():
            try:
                customer = stripe.Customer.create(
                    email=form.cleaned_data['email'],
                    card=form.cleaned_data['stripe_id'],
                    plan='TBY_MONTHLY',
                )

                if customer:
                    # save user data to DB
                    user = form.save()
                    # hash password with set_password
                    password = request.POST.get('password1')
                    user.set_password(password)
                    user.stripe_id = customer.stripe_id
                    user.subscription_end = arrow.now().replace(weeks=+4).datetime
                    user.save()

                    # if 'image' in request.FILES:
                    #    profile.image = request.FILES['image']

                    user = auth.authenticate(username=request.POST.get('username'),
                                             password=request.POST.get('password1'))

                    if user:
                        auth.login(request, user)
                        messages.success(request, "Thank you for registering")
                        return redirect(reverse('profile'))

                    else:
                        messages.error(request, "We were unable to log you in at this time")

                else:
                    messages.error(request, "We were unable to take payment from the card provided")
            except stripe.error.CardError, e:
                messages.error(request, "Sorry. Your card was declined")

        else:
            print(form.errors)

    else:
        today = datetime.date.today()
        form = UserRegistrationForm(initial={'expiry_month': today.month, 'expiry_year': today.year})

    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE}
    args.update(csrf(request))
    return render(request, 'accounts/register.html', args)


@login_required(login_url='/accounts/login/')
def cancel_subscription(request):
    try:
        customer = stripe.Customer.retrieve(request.user.stripe_id)

        customer.cancel_subscription(at_period_end=True)
    except Exception, e:
        messages.error(request, e)

    return redirect('profile')


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your Username and, or Password was not recognised")

    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'accounts/login.html', args)


def logout(request):
    auth.logout(request)
    return redirect(reverse('home'))


def profile(request):
    # this view needs extending (change bio to something better and access all UserProfile attributes from it)
    # will probably use this for dashboard fitness app. How can other users view???
    '''profile_user = request.user.id
    bio = UserProfile.objects.get(user_id=profile_user)
    bio = bio.bio
    args = {'bio': bio}'''
    return render(request, 'accounts/profile.html')

