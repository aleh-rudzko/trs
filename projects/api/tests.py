from datetime import timedelta

from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.models import Permission, User

from rest_framework import status
from rest_framework.test import APITestCase

from projects.factories import UserFactory, AdminFactory, GroupFactory, ProjectFactory, TaskFactory
from projects.models import Project, Task


class ProjectViewSetTests(APITestCase):
    def test_create_project_as_admin(self):
        url = reverse('project-list')
        data = {
            'name': 'test',
            'start_date': timezone.now(),
            'description': 'test',
            'end_date': timezone.now()
        }

        user = AdminFactory()
        self.client.force_login(user)

        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 1)

        project = Project.objects.get()
        self.assertEqual(project.name, 'test')

    def test_create_project_as_anonymous(self):
        url = reverse('project-list')
        data = {
            'name': 'test',
            'start_date': timezone.now() + timedelta(days=5),
            'end_date': timezone.now(),
            'description': 'Test description'
        }

        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Project.objects.count(), 0)

    def test_create_project_as_user(self):
        url = reverse('project-list')
        data = {
            'name': 'test',
            'start_date': timezone.now(),
            'description': 'test',
            'end_date': timezone.now()
        }
        user = UserFactory()
        self.client.force_login(user)

        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Project.objects.count(), 0)

    def test_create_project_with_invalid_range_between_start_and_end_date(self):
        url = reverse('project-list')
        data = {
            'name': 'test',
            'start_date': timezone.now() + timedelta(days=5),
            'end_date': timezone.now(),
            'description': 'Test description'
        }

        user = AdminFactory()
        self.client.force_login(user)

        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'non_field_errors': ['End date must occur after start date']})
        self.assertEqual(Project.objects.count(), 0)

    def test_get_projects_as_admin(self):
        ProjectFactory.create_batch(size=5)

        user = AdminFactory()
        self.client.force_login(user)

        url = reverse('project-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
        self.assertEqual(len(Project.objects.available_for_user(user)), len(response.data))

    def test_get_projects_as_owner(self):
        project, *_ = ProjectFactory.create_batch(size=4)

        self.client.force_login(project.owner)

        url = reverse('project-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Project.objects.filter(owner=project.owner).count(), len(response.data))
        self.assertEqual(Project.objects.available_for_user(project.owner).count(), len(response.data))
        self.assertEqual(project.name, response.data[0]['name'])

    def test_get_projects_as_user(self):
        user = UserFactory()
        project, *_ = ProjectFactory.create_batch(size=5)
        project.memberships.create(user=user)

        self.client.force_login(user)

        url = reverse('project-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Project.objects.filter(memberships__user=user).count(), len(response.data))
        self.assertEqual(Project.objects.available_for_user(project.owner).count(), len(response.data))
        self.assertEqual(project.name, response.data[0]['name'])

    def test_get_projects_as_anonymous(self):
        ProjectFactory.create_batch(size=5)

        url = reverse('project-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, {'detail': 'Authentication credentials were not provided.'})

    def test_get_project_as_admin(self):
        project, *_ = ProjectFactory.create_batch(size=5)
        url = reverse('project-detail', args=(project.pk,))

        user = AdminFactory()
        self.client.force_login(user)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(len(Project.objects.available_for_user(user)), 0)

    def test_get_project_as_owner(self):
        project = ProjectFactory()
        url = reverse('project-detail', args=(project.pk,))
        self.client.force_login(project.owner)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Project.objects.get(pk=project.pk).name, response.data['name'])

    def test_get_project_as_user(self):
        user = UserFactory()
        self.client.force_login(user)

        project = ProjectFactory()
        url = reverse('project-detail', args=(project.pk,))

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'detail': 'Not found.'})

    def test_get_project_as_membership(self):
        user = UserFactory()
        self.client.force_login(user)

        project = ProjectFactory()
        project.memberships.create(user=user)
        url = reverse('project-detail', args=(project.pk,))

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Project.objects.get(pk=project.pk).name, response.data['name'])

    def test_get_project_as_anonymous(self):
        project, *_ = ProjectFactory.create_batch(size=5)
        url = reverse('project-detail', args=(project.pk,))

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, {'detail': 'Authentication credentials were not provided.'})

    def test_update_project_as_owner(self):
        project = ProjectFactory()
        url = reverse('project-detail', args=(project.pk,))
        self.client.force_login(project.owner)

        data = {
            'description': 'Updated description',
            'start_date': timezone.now(),
            'end_date': timezone.now(),
            'name': 'Update name'
        }

        response = self.client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Project.objects.get(pk=project.pk).description, response.data['description'])

    def test_update_project_as_admin(self):
        project = ProjectFactory()
        url = reverse('project-detail', args=(project.pk,))

        user = AdminFactory()
        self.client.force_login(user)

        data = {
            'description': 'Updated description',
            'start_date': timezone.now(),
            'end_date': timezone.now(),
            'name': 'Update name'
        }

        response = self.client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_project_as_user(self):
        project = ProjectFactory()
        url = reverse('project-detail', args=(project.pk,))

        user = UserFactory()
        self.client.force_login(user)

        data = {
            'description': 'Updated description'
        }
        response = self.client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Project.objects.get(pk=project.pk).description, project.description)

    def test_update_project_as_anonymous(self):
        project = ProjectFactory()
        url = reverse('project-detail', args=(project.pk,))

        data = {
            'description': 'Updated description'
        }
        response = self.client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Project.objects.get(pk=project.pk).description, project.description)


class TaskViewSetTests(APITestCase):
    def test_get_tasks_as_owner(self):
        task, *_ = TaskFactory.create_batch(size=5)
        self.client.force_login(task.owner)

        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.filter(owner=task.owner).count(), len(response.data))
        self.assertEqual(Task.objects.available_for_user(task.owner).count(), len(response.data))
        self.assertEqual(task.name, response.data[0]['name'])

    def test_get_tasks_as_member(self):
        user = UserFactory()
        self.client.force_login(user)

        task1, task2, task3, *_ = TaskFactory.create_batch(size=5)
        task1.memberships.create(user=user)
        task2.memberships.create(user=user)
        task3.memberships.create(user=user, is_active=False)

        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Task.objects.filter(memberships__user=user, memberships__is_active=True).count(), len(response.data))
        self.assertEqual(Task.objects.available_for_user(user).count(), len(response.data))

    def test_get_tasks_as_project_owner(self):
        task, *_ = TaskFactory.create_batch(size=5)
        self.client.force_login(task.project.owner)

        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.filter(project__owner=task.project.owner).count(), len(response.data))
        self.assertEqual(Task.objects.available_for_user(task.project.owner).count(), len(response.data))

    def test_get_tasks_as_anonymous(self):
        TaskFactory.create_batch(size=5)

        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, {'detail': 'Authentication credentials were not provided.'})

    def test_create_task(self):
        project = ProjectFactory()
        permissions = Permission.objects.filter(codename__in=['add_task'])
        group = GroupFactory.create(permissions=permissions)
        project.owner.groups.add(group)
        self.client.force_login(project.owner)

        url = reverse('task-list')
        data = {
            'name': 'Name',
            'description': 'Description',
            'start_date': timezone.now(),
            'end_date': timezone.now(),
            'project': project.pk
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.get().name, data['name'])


# class ReportViewSet(APITestCase):
