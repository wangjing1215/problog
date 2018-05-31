"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from DjangoUeditor import urls as djud_urls
from . import testdb, view, search, logon, addarctic
from blog import views
from django.conf import settings
urlpatterns = [
    url(r'^$', view.hello),
    url(r'^admin/', admin.site.urls),
    url(r'^testdb$', testdb.testdb),
    url(r'^adddate$', testdb.adddata),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^post$', search.search_post),
    url(r'^logon$', logon.logon),
    url(r'^signin$', logon.signin),
    url(r'^hello$', views.blog_index),
    url(r'^ueditor/', include(djud_urls)),
    url(r'^add$', addarctic.add),
    url(r'^indexfor$', views.blog_hello),
    url(r'^eveblog/$', views.eveblog),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)