from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'index.html', context)
def add(request):
    return render(request, 'add.html')