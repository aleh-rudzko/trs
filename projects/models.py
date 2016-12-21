from django.db import models
from django.db.models import Q

from trs.mixins import TimeStampModel
from users.models import User


class ProjectManager(models.Manager):
    def available_for_user(self, user):
        queryset = self.filter(
            Q(memberships__user=user, memberships__is_active=True) | Q(owner=user))
        return queryset


class Project(TimeStampModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    owner = models.ForeignKey(User, related_name='projects')

    objects = ProjectManager()

    @models.permalink
    def get_absolute_url(self):
        return 'project_detail', (self.pk, )

    def __str__(self):
        return self.name


class ProjectMembership(TimeStampModel):
    LEVELS = (
        (0, 'Member'),
        (1, 'Manager'),
        (2, 'Admin')
    )

    user = models.ForeignKey(User, verbose_name='user', related_name='project_memberships')
    project = models.ForeignKey(Project, verbose_name='project', related_name='memberships')
    is_active = models.BooleanField(verbose_name='is_active', default=True)
    role = models.IntegerField(choices=LEVELS, default=0)

    def __str__(self):
        return '%s user invited to project %s' % (self.user, self.project)


class TaskManager(models.Manager):
    def available_for_user(self, user):
        queryset = self.filter(
            Q(memberships__user=user, memberships__is_active=True) |
            Q(owner=user) |
            Q(project__memberships__user=user, project__memberships__role__in=[1, 2],
              project__memberships__is_active=True) | Q(project__owner=user))
        return queryset


class Task(TimeStampModel):
    STATES = (
        (0, 'Draft'),
        (1, 'Start'),
        (2, 'Completed')
    )
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    state = models.IntegerField(choices=STATES, default=0)
    project = models.ForeignKey(Project, related_name='tasks')
    owner = models.ForeignKey(User, related_name='tasks')
    objects = TaskManager()

    @models.permalink
    def get_absolute_url(self):
        return 'project_task_detail', [self.project.pk, self.pk, ]

    def __str__(self):
        return 'Task "%s" for project "%s"' % (self.name, self.project.name)


class TaskMembership(TimeStampModel):
    user = models.ForeignKey(User, verbose_name='user')
    task = models.ForeignKey(Task, verbose_name='task', related_name='memberships')
    is_active = models.BooleanField(verbose_name='is_active', default=True)


class Report(TimeStampModel):
    report_date = models.DateTimeField()
    effort = models.TimeField()
    description = models.TextField(max_length=200)
    task = models.ForeignKey(Task, related_name='reports')
    user = models.ForeignKey(User, related_name='reports')
