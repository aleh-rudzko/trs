from django.db import models

# Create your models here.
from trs.mixins import TimeStampModel
from projects.models import Project
from users.models import User


class Task(TimeStampModel):
    STATE = (
        (0, 'Draft'),
        (1, 'Start'),
        (2, 'Completed')
    )
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    state = models.IntegerField(choices=STATE, default=0)
    project = models.ForeignKey(Project)
    owner = models.ForeignKey(User)
    employees = models.ManyToManyField(User, related_name='available_tasks')

    def is_membership(self, user):
        return self.taskmembership_set.filter(user=user).count() > 0

    def is_owner(self, user):
        return self.owner == user


class TaskMembership(TimeStampModel):
    user = models.ForeignKey(User, verbose_name='user')
    task = models.ForeignKey(Task, verbose_name='task')
    is_active = models.BooleanField(verbose_name='is_active', default=True)

