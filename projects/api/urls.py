__author__ = 'Aleh'

from rest_framework import routers
from projects.api.views import ProjectViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
urlpatterns = router.urls
