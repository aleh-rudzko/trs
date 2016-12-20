from rest_framework import viewsets
from rest_framework import permissions
from projects.models import Project, Task, Report, ProjectMembership, TaskMembership
from projects.api.serializers import ProjectSerializer, ProjectMembershipSerializer
from projects.api.serializers import TaskSerializer, TaskMembershipSerializer
from projects.api.serializers import ReportSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Project.objects.available_for_user(self.request.user)
        return Project.objects.none()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProjectMembershipViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectMembershipSerializer
    queryset = ProjectMembership.objects.all()


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskMembershipViewSet(viewsets.ModelViewSet):
    serializer_class = TaskMembershipSerializer
    queryset = TaskMembership.objects.all()


class ReportViewSet(viewsets.ModelViewSet):
    serializer_class = ReportSerializer
    queryset = Report.objects.all()