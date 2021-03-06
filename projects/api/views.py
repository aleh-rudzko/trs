from rest_framework import viewsets
from rest_framework import permissions

from projects.api.permissions import IsAdminProjectOrReadOnly
from projects.models import Project, Task, Report, ProjectMembership, TaskMembership
from projects.api.serializers import ProjectSerializer, ProjectMembershipSerializer
from projects.api.serializers import TaskSerializer, TaskMembershipSerializer
from projects.api.serializers import ReportSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated, IsAdminProjectOrReadOnly)

    def get_queryset(self):
        return Project.objects.available_for_user(self.request.user)


class ProjectMembershipViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectMembershipSerializer
    queryset = ProjectMembership.objects.all()


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return Task.objects.available_for_user(self.request.user)


class TaskMembershipViewSet(viewsets.ModelViewSet):
    serializer_class = TaskMembershipSerializer
    queryset = TaskMembership.objects.all()


class ReportViewSet(viewsets.ModelViewSet):
    serializer_class = ReportSerializer
    queryset = Report.objects.all()