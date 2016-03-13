from rest_framework import routers
from projects.api.views import ProjectViewSet, TaskViewSet, ReportViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'reports', ReportViewSet)
urlpatterns = router.urls
