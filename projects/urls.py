from django.conf.urls import url
from projects.views import ProjectListView, ProjectDetailView, ProjectTaskListView, ProjectTaskDetailView

__author__ = 'Aleh'

urlpatterns = [
    url(r'^$', ProjectListView.as_view(), name='project_list'),
    url(r'^(?P<pk>[\d]+)/$', ProjectDetailView.as_view(), name='project_detail'),
    url(r'^(?P<pk>[\d]+)/task/$', ProjectTaskListView.as_view(), name='project_task_list'),
    url(r'^(?P<pk>[\d]+)/task/(?P<task_pk>[\d]+)/$', ProjectTaskDetailView.as_view(), name='project_task_detail')
]