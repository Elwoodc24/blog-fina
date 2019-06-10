# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Blog

# Create your views here.

def index(request):
    blogs = Blog.objects.order_by('-date')
    context = {'blogs': blogs}
    return render(request, 'blog_app/index.html', context)

def blog(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    context = {'blog': blog}
    return render(request, 'blog_app/blog.html', context)
