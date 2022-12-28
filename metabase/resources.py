from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound

from .models import EmbeddedReport
from .serializers import EMBEDDED_REPORT_LIST_PREPARER

from rest_framework.exceptions import PermissionDenied

from rest_framework.viewsets import GenericViewSet
# from rest_framework.mixins import PaginatorMixin
# from rest_framework.views import APIView

EMBEDDED_REPORT_NOT_FOUND = "Embedded report not found."

def permissions(needs):
    def wrapper(func):
        def inner_func(self, *args, **kwargs):
            # Check whether the user has the required permissions
            if not self.request.user.has_perms(needs):
                raise PermissionDenied
            # Call the original resource method if the user has the required permissions
            return func(self, *args, **kwargs)
        return inner_func
    return wrapper

class EmbeddedReportResource(GenericViewSet):
    preparer = EMBEDDED_REPORT_LIST_PREPARER
    paginate = True
    page_size = 40

    @property
    def base_query(self):
        return (
            EmbeddedReport.objects.filter(active=True)
            .select_related("engine")
            .order_by("name")
        )

    def prepare(self, data):
        result = super().prepare(data)
        if self.endpoint == "detail":
            result["url"] = data.get_report_url_for_business(self.business)
        return result

    @permissions(needs=("embedded-report-list",))
    def list(self):
        return self.base_query

    @permissions(needs=("embedded-report-list",))
    def detail(self, pk):
        return self.get_or_error(self.base_query, EMBEDDED_REPORT_NOT_FOUND, pk=pk)