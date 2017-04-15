# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import get_object_or_404


def post_list(request):
    # view will return a list of Posts and order by date_published
    posts = Post.objects.filter(date_published__lte=timezone.now()).order_by('-date_published')
    args = {'posts': posts}
    return render(request, 'blog/blogposts.html', args)


def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    args = {'post': post}
    return render(request, 'blog/postdetails.html', args)