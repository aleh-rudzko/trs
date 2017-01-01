from datetime import timedelta

import factory
from django.contrib.auth.models import Group
from django.utils import timezone

from projects.models import Project, Task, Report
from users.models import User


class GroupFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: "Group %s".format(n))

    @factory.post_generation
    def permissions(self, created, extracted, **kwargs):
        if not created:
            return

        if extracted:
            self.permissions.add(*extracted)

    class Meta:
        model = Group


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Sequence(lambda n: "oleg.unsav+{}@gmail.com".format(n))
    password = 'test'
    is_active = True

    class Meta:
        model = User


class AdminFactory(UserFactory):
    is_admin = True


class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project

    name = factory.Sequence(lambda n: "Project {}".format(n))
    description = factory.Sequence(lambda n: "Project description {}".format(n))
    start_date = timezone.now() - timedelta(days=5)
    end_date = timezone.now() + timedelta(days=5)

    owner = factory.SubFactory(AdminFactory)


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    name = factory.Sequence(lambda n: 'Task {}'.format(n))
    description = factory.Sequence(lambda n: 'Task description {}'.format(n))
    owner = factory.SubFactory(UserFactory)
    project = factory.SubFactory(ProjectFactory)
    start_date = timezone.now()
    end_date = timezone.now()


class ReportFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Report
