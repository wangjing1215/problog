
# -*- coding: utf-8 -*-
from django.shortcuts import render
from blog.models import Article
import re
from django.http import HttpResponse
# Create your views here.
def blog_index(request):
    blog_list = Article.objects.all()  # 获取所有数据
    return render(request, 'hello.html', {'blog_list': blog_list})   # 返回index.html
def blog_hello(request):
    blog_list = Article.objects.all()  # 获取所有数据
    p = r'<p><img.+</p>'
    return render(request, 'indexfor.html', {'blog_list': blog_list})   # 返回index.html
def eveblog(request):
    idget = request.GET['id']
    blog = Article.objects.filter(id=idget)
    return render(request, 'hello.html', {'blog_list': blog})   # 返回index.html


