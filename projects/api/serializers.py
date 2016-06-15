from rest_framework import serializers
from projects.models import Project, Task, Report, ProjectMembership, TaskMembership
from users.models import User


class ProjectSerializer(serializers.ModelSerializer):
    tasks = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='task-detail'
    )
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Project


class ProjectMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMembership


class TaskMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskMembership


class TaskSerializer(serializers.ModelSerializer):
    reports = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='report-detail'
    )

    class Meta:
        model = Task


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
