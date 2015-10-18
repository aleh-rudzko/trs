from django.shortcuts import render
from django.views.generic import ListView, DetailView
from projects.models import Project
# Create your views here.

class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    paginate_by = 10
    template_name = 'projects/project_list.html'

    def get_queryset(self):
        return Project.objects.available_for_user(self.request.user)

class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'projects/project_detail.html'


