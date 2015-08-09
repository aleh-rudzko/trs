from django.db import models

# Create your models here.
from TS.mixins import TimeStampModel
from tasks.models import Task
from users.models import User

class Report(TimeStampModel):
    report_date = models.DateTimeField()
    effort = models.TimeField()
    description = models.TextField(max_length=200)
    tasks = models.ForeignKey(Task, related_name='reports')
    user = models.ForeignKey(User, related_name='reports')
