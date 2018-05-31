# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views.decorators import csrf
from blog.models import Article
import time
import re
def add(request):
    user =''
    nt = time.asctime( time.localtime(time.time()) )
    if request.POST:
        if request.POST.has_key('_save'):
            addblog= Article()
            addblog.category = request.POST['category']
            addblog.content = request.POST['content']

            p = r'<p>(<img src=.+\.jpg)'
            pp = re.compile(p)
            pic = pp.findall(addblog.content)
            if pic == []:
                addblog.picture = 0
            else:
                for j in pic:
                    addblog.picture = j+'/>'
                    break
            if (Article.objects.filter(category=request.POST['category']).filter(content=request.POST['content'])):
                addblog.update_time = nt
            else:
                addblog.pub_date = nt
            addblog.title = request.POST['title']
            addblog.save()
            return HttpResponseRedirect("/hello")
        if request.POST.has_key('_addanother'):
            addblog= Article()
            addblog.category = request.POST['category']
            addblog.content = request.POST['content']
            if (Article.objects.filter(category=request.POST['category']).filter(content=request.POST['content'])):
                addblog.update_time = nt
            else:
                addblog.pub_date = nt
            addblog.title = request.POST['title']
            addblog.save()
            return HttpResponseRedirect("/add")
    return render(request, "add.html")