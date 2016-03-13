from rest_framework import viewsets
from projects.api.serializers import ProjectSerializer, TaskSerializer, ReportSerializer
from projects.models import Project, Task, Report


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class ReportViewSet(viewsets.ModelViewSet):
    serializer_class = ReportSerializer
    queryset = Report.objects.all()