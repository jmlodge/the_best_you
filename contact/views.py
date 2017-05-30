# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from contact.forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template


def contact(request):
    form = ContactForm

    if request.method == 'POST':
        form = form(data=request.POST)

        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            content = request.POST.get('content')

            template = get_template('contact/contacttemplate.txt')
            context = {'name': name,
                       'email': email,
                       'content': content}

            all_content = template.render(context)

            email_message = EmailMessage('New contact submission', all_content, 'Website' + '',
                                         ['josephmartinlodge@gmail.com'],
                                         headers={'Reply to': email})
            email_message.send()
            return redirect('contact')

    return render(request, 'contact/contact.html', {'form': form})

