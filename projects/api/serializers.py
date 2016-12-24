from rest_framework import serializers
from projects.models import Project, Task, Report, ProjectMembership, TaskMembership


class ProjectSerializer(serializers.ModelSerializer):
    tasks = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='task-detail'
    )
    owner = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError('End date must occur after start date')
        return data

    class Meta:
        model = Project
        fields = '__all__'


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
    owner = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    def validate_project(self, project):
        user = self.context.get('request').user
        if not project.is_manager(user):
            raise serializers.ValidationError('You cannot create task in this project')
        return project

    def validate(self, data):
        start_date = data['start_date']
        end_date = data['end_date']
        if start_date > end_date:
            raise serializers.ValidationError('End date must occur after start date')

        project = data['project']
        if project.start_date > start_date or project.end_date < end_date:
            raise serializers.ValidationError('Task period not in project period')

        return data

    class Meta:
        model = Task
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
