# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from contact.forms import ContactForm


def contact(request):
    form = ContactForm

    return render(request, 'contact/contact.html', {'form': form})

