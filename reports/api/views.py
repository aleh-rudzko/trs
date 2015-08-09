from rest_framework import viewsets
from reports.api.serializers import ReportSerializer
from reports.models import Report

class ReportViewSet(viewsets.ModelViewSet):
    serializer_class = ReportSerializer
    queryset = Report