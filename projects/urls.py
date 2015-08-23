from django.conf.urls import patterns, url
from projects.views import ProjectListView

__author__ = 'Aleh'

urlpatterns = patterns('projects.views',
    url(r'^$', ProjectListView.as_view(), name='projects-list')
)