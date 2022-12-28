from rest_framework import generics
from .models import EmbeddedReport
from .serializers import EmbeddedReportSerializer

class EmbeddedReportListView(generics.ListAPIView):
    queryset = EmbeddedReport.objects.all()
    serializer_class = EmbeddedReportSerializer

class EmbeddedReportDetailView(generics.RetrieveAPIView):
    queryset = EmbeddedReport.objects.all()
    serializer_class = EmbeddedReportSerializer