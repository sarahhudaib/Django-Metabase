from rest_framework import serializers
from .models import EmbeddedReport


class EmbeddedReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmbeddedReport
        fields = ["id", "name", "engine", "reference_id", "reference_type", "active"]

EMBEDDED_REPORT_LIST_PREPARER = EmbeddedReportSerializer