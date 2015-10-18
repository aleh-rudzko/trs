from django.db import models
from TS.mixins import TimeStampModel
from users.models import User
# Create your models here.

class ProjectManager(models.Manager):
    def available_for_user(self, user):
        queryset = self.filter(projectmembership__user=user, projectmembership__is_active=True)
        return queryset

    def available_for_admin(self, user):
        queryset = self.filter(admin=user)
        return queryset


class Project(TimeStampModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    owner = models.ForeignKey(User, related_name='projects')
    employees = models.ManyToManyField(User, related_name='available_projects')

    objects = ProjectManager()

    @models.permalink
    def get_absolute_url(self):
        return 'project_detail', [self.pk,]

    def __str__(self):
        return self.name

    def is_owner(self, user):
        return self.owner == user

    def is_admin(self, user):
        return self.projectmembership_set.filter(user=user, role='Admin').count() > 0

    def is_manager(self, user):
        return self.is_admin(user) or self.projectmembership_set.filter(user=user, role='Manager').count() > 0

    def is_membership(self, user):
        return self.is_manager(user) or self.projectmembership_set.filter(user=user, role='Member').count() > 0

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