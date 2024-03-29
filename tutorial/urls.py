"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', 'principal.views.index', name='index'),
    
    url(r'^djpython/', include('principal.urls',namespace="encuesta")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^crear/', 'principal.views.crear', name='crear'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
    url(r'^api/posts/', include('principal.api.urls',namespace="posts-api")),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

