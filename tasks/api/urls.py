from rest_framework import routers
from tasks.api.views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
urlpatterns = router.urls