from rest_framework import viewsets
from tasks.api.serializers import TaskSerializer
from tasks.models import Task

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()