# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views.decorators import csrf
from blog.models import User

def logon(request):
    user =''
    if request.POST:
        if (User.objects.filter(name=request.POST['username']).filter(password=request.POST['password'])):
            user1 = User.objects.filter(name=request.POST['username']).filter(password=request.POST['password'])
            return HttpResponseRedirect("/indexfor")
        else:
            msg = 'uesrname/password is wrong.please try again!'
            return render(request, "logon.html", {'msg':msg})
    return render(request, "logon.html")
def signin(request):
    if request.POST:
        adduser=User()
        adduser.name = request.POST['username']
        if (User.objects.filter(name=request.POST['username'])):
            msg = 'this name has existed,srory!try a good one!'
            return render(request, "signup.html", {'msg':msg})
        if request.POST['username'] in ['Username','username'] and request.POST['password']=='password':
            msg = 'username can not be blank'
            return render(request, "signup.html", {'msg':msg})
        adduser.password = request.POST['password']
        adduser.save()
        msg = 'sign in ok,please log on!'
        return render(request, "logon.html", {'msg':msg})
    return render(request, "signup.html")