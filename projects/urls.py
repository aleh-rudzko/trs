from django.conf.urls import patterns, url
from projects.views import ProjectListView, ProjectDetailView

__author__ = 'Aleh'

urlpatterns = patterns('projects.views',
    url(r'^$', ProjectListView.as_view(), name='project_list'),
    url(r'^(?P<pk>[\d]+)/$', ProjectDetailView.as_view(), name='project_detail')
)