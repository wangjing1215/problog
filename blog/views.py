
# -*- coding: utf-8 -*-
from django.shortcuts import render
from blog.models import Article


# Create your views here.
def blog_index(request):
    blog_list = Article.objects.all()  # 获取所有数据
    return render(request, 'hello.html', {'blog_list':blog_list})   # 返回index.html
