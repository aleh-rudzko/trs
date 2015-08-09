from django.db import models
from TS.mixins import TimeStampModel
from users.models import User
# Create your models here.


class Project(TimeStampModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    admin = models.ForeignKey(User, related_name='projects')
    employees = models.ManyToManyField(User, related_name='available_projects')