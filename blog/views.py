# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect
from forms import BlogForm


def post_list(request):
    # view will return a list of Posts and order by date_published
    posts = Post.objects.filter(date_published__lte=timezone.now()).order_by('-date_published')
    args = {'posts': posts}
    return render(request, 'blog/blogposts.html', args)


def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    post.views += 1  # this will count the number of times a post is viewed
    post.save()
    args = {'post': post}
    return render(request, 'blog/postdetails.html', args)


def new_post(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date_published = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogForm()
    return render(request, 'blog/blogform.html', {'form': form})


def edit_post(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date_published = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogForm(instance=post)
    return render(request, 'blog/blogform.html', {'form': form})

