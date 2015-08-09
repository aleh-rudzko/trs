__author__ = 'Aleh'

from reports.api.views import ReportViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'reports', ReportViewSet)
urlpatterns = router.urls
