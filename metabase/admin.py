from django.contrib import admin
from .models import EmbeddedReport, ReportEngine

# Register your models here.

# 1. To customize the way the model is displayed in the admin interface.
class EmbeddedReportAdmin(admin.ModelAdmin):
    list_display = ['name']

class ReportEngineAdmin(admin.ModelAdmin):
    list_display = ['name']

    
# 2. Register the models with the admin interface
admin.site.register(EmbeddedReport, EmbeddedReportAdmin)
admin.site.register(ReportEngine, ReportEngineAdmin)

