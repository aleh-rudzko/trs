from rest_framework import routers

from projects.api.views import ProjectViewSet, ProjectMembershipViewSet
from projects.api.views import TaskViewSet, TaskMembershipViewSet
from projects.api.views import ReportViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet, base_name='project')
router.register(r'project_memberships', ProjectMembershipViewSet)
router.register(r'tasks', TaskViewSet, base_name='task')
router.register(r'task_memberships', TaskMembershipViewSet)
router.register(r'reports', ReportViewSet)
urlpatterns = router.urls
