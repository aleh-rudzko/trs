from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from projects.models import Project, Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
# Create your views here.


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    paginate_by = 10
    context_object_name = 'projects'
    template_name = 'projects/project_list.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_admin():
            return Project.objects.available_for_admin(user)
        return Project.objects.available_for_user(user)


class BaseProjectDetail(LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, pk=kwargs['pk'])
        if not self.project.verify_access(request.user):
            raise PermissionDenied()
        return super(BaseProjectDetail, self).get(request, *args, **kwargs)


class ProjectDetailView(BaseProjectDetail, DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'projects/project_detail.html'


class ProjectTaskListView(BaseProjectDetail, ListView):
    context_object_name = 'tasks'
    template_name = 'tasks/task_list.html'

    def get_queryset(self):
        user = self.request.user
        if self.project.is_manager(user):
            return Task.objects.filter(project=self.project)
        return Task.objects.available_for_user(user).filter(project=self.project)


class BaseTaskDetail(BaseProjectDetail):
    def get(self, request, *args, **kwargs):
        self.task = get_object_or_404(Task, pk=kwargs['task_pk'])
        if not self.task.verify_access(request.user):
            raise PermissionDenied()
        return super(BaseTaskDetail, self).get(request, *args, **kwargs)


class ProjectTaskDetailView(BaseTaskDetail, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_detail.html'


class TaskReportListView(BaseTaskDetail, ListView):
    context_object_name = 'reports'
    template_name = 'reports/report_list.html'

    def get_queryset(self):
        user = self.request.user




