from django.apps import AppConfig
from django.db.models.signals import post_save

from projects.signals import add_owner_as_membership


class ProjectConfig(AppConfig):
    name = 'projects'

    def ready(self):
        project_model = self.get_model('Project')
        post_save.connect(add_owner_as_membership, project_model)
