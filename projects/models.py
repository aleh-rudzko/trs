from django.db import models
from trs.mixins import TimeStampModel
from users.models import User


class ProjectManager(models.Manager):
    def available_for_user(self, user):
        queryset = self.filter(memberships__user=user, memberships__is_active=True)
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

    def is_owner(self, user):
        return self.owner == user

    def verify_access(self, user):
        return self.is_membership(user)

    def is_admin(self, user):
        admin_level = 2
        return self.check_role(user, admin_level)

    def is_manager(self, user):
        manager = [1, 2]
        return self.check_role(user, manager)

    def is_membership(self, user):
        membership = [0, 1, 2]
        return self.check_role(user, membership)

    def check_role(self, user, role):
        query = {
            'user': user,
            'is_active': True
        }
        if isinstance(role, list):
            query['role__in'] = role
        else:
            query['role'] = role

        return self.memberships.filter(**query).exists()


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
        queryset = self.filter(taskmembership__user=user, taskmembership__is_active=True)
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

    def is_membership(self, user):
        return self.taskmembership_set.filter(user=user).exists()

    def is_owner(self, user):
        return self.owner == user

    def verify_access(self, user):
        return self.is_membership(user) or self.is_owner(user) or self.project.is_manager(user)

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
    task = models.ForeignKey(Task, related_name='reports')
    user = models.ForeignKey(User, related_name='reports')
