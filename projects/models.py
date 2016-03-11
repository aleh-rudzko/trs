from django.db import models
from trs.mixins import TimeStampModel
from users.models import User
# Create your models here.

class ProjectManager(models.Manager):
    def available_for_user(self, user):
        queryset = self.filter(projectmembership__user=user, projectmembership__is_active=True)
        return queryset

    def available_for_admin(self, user):
        queryset = self.filter(owner=user)
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
        return 'project_detail', [self.pk,]

    def __str__(self):
        return self.name

    def is_owner(self, user):
        return self.owner == user

    def is_admin(self, user):
        conditions = [
            self.is_owner(user),
            self.projectmembership_set.filter(user=user, role=2, is_active=True).exists()
        ]
        return any(conditions)

    def is_manager(self, user):
        conditions = [
            self.is_admin(user),
            self.projectmembership_set.filter(user=user, role=1, is_active=True).exists()
        ]
        return any(conditions)

    def is_membership(self, user):
        conditions = [
            self.is_manager(user),
            self.projectmembership_set.filter(user=user, role=0, is_active=True).exists()
        ]
        return any(conditions)

    def verify_access(self, user):
        return self.is_membership(user)

class ProjectMembership(TimeStampModel):
    LEVELS = (
        (0, 'Member'),
        (1, 'Manager'),
        (2, 'Admin')
    )

    user = models.ForeignKey(User, verbose_name='user')
    project = models.ForeignKey(Project, verbose_name='project')
    is_active = models.BooleanField(verbose_name='is_active', default=True)
    role = models.IntegerField(choices=LEVELS, default=0)

    def __str__(self):
        return '%s user invited to project %s' % (self.user, self.project)


class TaskManager(models.Manager):
    def available_for_user(self, user):
        queryset = self.filter(taskmembership__user=user, taskmembership__is_active=True)
        return queryset


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
    objects = TaskManager()

    @models.permalink
    def get_absolute_url(self):
        return 'project_task_detail', [self.project.pk, self.pk, ]

    def is_membership(self, user):
        return self.taskmembership_set.filter(user=user).exists()

    def is_owner(self, user):
        return self.owner == user

    def verify_access(self, user):
        conditions_access = [
            self.is_owner(user),
            self.is_membership(user),
            self.project.is_manager(user)
        ]
        if any(conditions_access):
            return True
        return False

    def __str__(self):
        return 'Task "%s" for project "%s"' % (self.name, self.project.name)


class TaskMembership(TimeStampModel):
    user = models.ForeignKey(User, verbose_name='user')
    task = models.ForeignKey(Task, verbose_name='task')
    is_active = models.BooleanField(verbose_name='is_active', default=True)


class Report(TimeStampModel):
    report_date = models.DateTimeField()
    effort = models.TimeField()
    description = models.TextField(max_length=200)
    tasks = models.ForeignKey(Task, related_name='reports')
    user = models.ForeignKey(User, related_name='reports')