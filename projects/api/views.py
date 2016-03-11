__author__ = 'Aleh'

from rest_framework import viewsets
from projects.api.serializers import ProjectSerializer
from projects.models import Project

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
