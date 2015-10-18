from django.contrib import admin
from projects.models import Project, ProjectMembership
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    pass

class ProjectMembershipAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectMembership, ProjectMembershipAdmin)