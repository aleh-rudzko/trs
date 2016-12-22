"""TS URL Configuration

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
from trs.views import home
from django.contrib import admin

api_urlpatterns= [
    url(r'^users/', include('users.api.urls')),
    url(r'', include('projects.api.urls')),
    #url(r'^tasks/', include('tasks.api.urls')),
    #url(r'^reports/', include('reports.api.urls')),
]


urlpatterns = [
    url(r'^$', home, name='home_page'),
    url(r'^users/', include('users.urls')),
    url(r'^projects/', include('projects.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(api_urlpatterns)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]