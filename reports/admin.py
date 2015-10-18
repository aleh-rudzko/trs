from django.contrib import admin
from reports.models import Report


class ReportAdmin(admin.ModelAdmin):
    pass


admin.site.register(Report, ReportAdmin)
