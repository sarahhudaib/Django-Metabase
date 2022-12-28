from rest_framework import viewsets
from .models import EmbeddedReport
from .serializers import EmbeddedReportSerializer

class EmbeddedReportViewSet(viewsets.ModelViewSet):
    queryset = EmbeddedReport.objects.all()
    serializer_class = EmbeddedReportSerializer