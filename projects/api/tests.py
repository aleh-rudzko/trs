from datetime import datetime

from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission

from rest_framework import status
from rest_framework.test import APITestCase

from projects.factories import UserFactory, GroupFactory, ProjectFactory
from projects.models import Project


class ProjectViewSetTests(APITestCase):
    def test_create_project(self):
        url = reverse('project-list')
        data = {
            'name': 'test',
            'start_date': datetime.now().isoformat(),
            'description': 'test',
            'end_date': datetime.now().isoformat()
        }

        permissions = Permission.objects.filter(codename__in=['add_project'])
        group = GroupFactory.create(permissions=permissions)
        user = UserFactory.create(groups=(group,))
        self.client.force_login(user)

        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 1)

        project = Project.objects.get()
        self.assertEqual(project.name, 'test')
        self.assertEqual(project.memberships.get().user, user)

    def test_create_project_denied(self):
        url = reverse('project-list')
        data = {
            'name': 'test',
            'start_date': datetime.now().isoformat(),
            'description': 'test',
            'end_date': datetime.now().isoformat()
        }
        user = UserFactory()
        self.client.force_login(user)

        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Project.objects.count(), 0)

    def test_get_projects(self):
        url = reverse('project-list')
        project = ProjectFactory()
        self.client.force_login(project.owner)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Project.objects.filter(owner=project.owner).count(), len(response.data))
        self.assertEqual(project.name, response.data[0]['name'])

    def test_get_mine_projects_as_owner(self):
        project, *_ = ProjectFactory.create_batch(size=4)

        self.client.force_login(project.owner)

        url = reverse('project-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Project.objects.filter(owner=project.owner).count(), len(response.data))

    def test_get_mine_projects_as_user(self):
        user = UserFactory()
        project, *_ = ProjectFactory.create_batch(size=5)
        project.memberships.create(user=user)

        self.client.force_login(user)

        url = reverse('project-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Project.objects.filter(memberships__user=user).count(), len(response.data))

    def test_get_projects_as_anonymous(self):
        ProjectFactory.create_batch(size=5)

        url = reverse('project-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, {'detail': 'Authentication credentials were not provided.'})

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

    def test_update_project(self):
        permissions = Permission.objects.filter(codename__in=['change_project'])
        group = GroupFactory.create(permissions=permissions)
        project = ProjectFactory()
        project.owner.groups.add(group)
        url = reverse('project-detail', args=(project.pk,))
        self.client.force_login(project.owner)

        data = {
            'description': 'Updated description'
        }

        response = self.client.patch(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Project.objects.get(pk=project.pk).description, response.data['description'])

    def test_update_project_denied(self):
        project = ProjectFactory()
        url = reverse('project-detail', args=(project.pk,))
        self.client.force_login(project.owner)

        data = {
            'description': 'Updated description'
        }
        response = self.client.patch(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Project.objects.get(pk=project.pk).description, project.description)