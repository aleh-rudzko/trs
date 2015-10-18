from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from projects.models import Project, Task
from django.core.exceptions import PermissionDenied
# Create your views here.

class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    paginate_by = 10
    template_name = 'projects/project_list.html'

    def get_queryset(self):
        return Project.objects.available_for_user(self.request.user)

class BaseProjectDetail(object):
    def get(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, pk=kwargs['pk'])
        if not self.project.is_membership(request.user):
            raise PermissionDenied()
        return super(BaseProjectDetail, self).get(request, *args, **kwargs)

class ProjectDetailView(BaseProjectDetail, DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'projects/project_detail.html'


class TaskListView(ListView, BaseProjectDetail):
    context_object_name = 'tasks'
    template_name = 'tasks/task_list.html'

    def get_queryset(self):
        return Task.objects.all(project=self.project)


