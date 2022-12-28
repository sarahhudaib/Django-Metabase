from django.urls import path
from . import views

# urlpatterns = [
#     path('embedded-reports/', views.EmbeddedReportListView.as_view(), name='embedded-report-list'),
#     path('embedded-reports/<int:pk>/', views.EmbeddedReportDetailView.as_view(), name='embedded-report-detail'),
# ]

from django.urls import include, path
from . import viewsets

urlpatterns = [
    path('embedded-reports/', viewsets.EmbeddedReportViewSet.as_view({'get': 'list'}), name='embedded-report-list'),
    path('embedded-reports/<int:pk>/', viewsets.EmbeddedReportViewSet.as_view({'get': 'retrieve'}), name='embedded-report-detail'),
]