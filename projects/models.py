from django.db import models
from django.db.models import Q
from model_utils import Choices
from model_utils.models import TimeStampedModel

from users.models import User


class ProjectManager(models.Manager):
    def available_for_user(self, user):
        queryset = self.filter(
            Q(memberships__user=user, memberships__is_active=True) | Q(owner=user))
        return queryset


class Project(TimeStampedModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    owner = models.ForeignKey(User, related_name='projects')

    objects = ProjectManager()

    def is_owner(self, user):
        return self.owner == user

    def is_admin(self, user):
        return (
            self.is_owner(user) or
            self.memberships.filter(user=user, role=ProjectMembership.ROLE.admin).exists()
        )

    def is_manager(self, user):
        return (
            self.is_admin(user) or
            self.memberships.filter(user=user, role=ProjectMembership.ROLE.manager).exists()
        )

    def is_member(self, user):
        return (
            self.is_admin(user) or
            self.is_manager(user) or
            self.memberships.filter(user=user, role=ProjectMembership.ROLE.member).exists()
        )

    @models.permalink
    def get_absolute_url(self):
        return 'project_detail', (self.pk, )

    def __str__(self):
        return self.name


class ProjectMembership(TimeStampedModel):
    ROLE = Choices(
        (0, 'member', 'member'),
        (1, 'manager', 'manager'),
        (2, 'admin', 'admin')
    )

    user = models.ForeignKey(User, verbose_name='user', related_name='project_memberships')
    project = models.ForeignKey(Project, verbose_name='project', related_name='memberships')
    is_active = models.BooleanField(verbose_name='is_active', default=True)
    role = models.IntegerField(choices=ROLE, default=ROLE.member)

    def __str__(self):
        return '%s user invited to project %s' % (self.user, self.project)


class TaskManager(models.Manager):
    def available_for_user(self, user):
        queryset = self.filter(
            Q(memberships__user=user, memberships__is_active=True) |
            Q(owner=user) |
            Q(~Q(project__memberships__role=ProjectMembership.ROLE.member), project__memberships__user=user,
              project__memberships__is_active=True) | Q(project__owner=user))
        return queryset


class Task(TimeStampedModel):
    STATES = Choices(
        (0, 'draft', 'draft'),
        (1, 'start', 'start'),
        (2, 'completed', 'completed')
    )
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    state = models.IntegerField(choices=STATES, default=STATES.draft)
    project = models.ForeignKey(Project, related_name='tasks')
    owner = models.ForeignKey(User, related_name='tasks')
    objects = TaskManager()

    @models.permalink
    def get_absolute_url(self):
        return 'project_task_detail', [self.project.pk, self.pk, ]

    def __str__(self):
        return 'Task "%s" for project "%s"' % (self.name, self.project.name)


class TaskMembership(TimeStampedModel):
    user = models.ForeignKey(User, verbose_name='user')
    task = models.ForeignKey(Task, verbose_name='task', related_name='memberships')
    is_active = models.BooleanField(verbose_name='is_active', default=True)


class ReportManager(models.Manager):
    def available_for_user(self, user):
        queryset = self.filter(
            Q(user=user) |
            Q(task__memberships__user=user, task__memberships__is_active=True) |
            Q(~Q(task__project__memberships__role=ProjectMembership.ROLE.member),
              task__project__memberships__user=user, task__project__memberships__is_active=True) |
            Q(task__project__owner=user))
        return queryset


class Report(TimeStampedModel):
    report_date = models.DateTimeField()
    effort = models.TimeField()
    description = models.TextField(max_length=200)
    task = models.ForeignKey(Task, related_name='reports')
    user = models.ForeignKey(User, related_name='reports')

    objects = ReportManager()