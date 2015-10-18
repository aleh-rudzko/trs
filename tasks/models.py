from django.db import models

# Create your models here.
from TS.mixins import TimeStampModel
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
    employees = models.ManyToManyField(User, related_name='available_tasks')
