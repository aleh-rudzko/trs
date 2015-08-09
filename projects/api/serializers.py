__author__ = 'Aleh'


from rest_framework import serializers
from projects.models import Project
from users.models import User

class ProjectSerializer(serializers.ModelSerializer):
    admin = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    employees = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Project