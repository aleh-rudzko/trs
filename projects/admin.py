from django.contrib import admin
from projects.models import Project, ProjectMembership, Task, TaskMembership


class ProjectAdmin(admin.ModelAdmin):
    pass


class ProjectMembershipAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectMembership, ProjectMembershipAdmin)


class TaskAdmin(admin.ModelAdmin):
    pass


class TaskMembershipAdmin(admin.ModelAdmin):
    pass

admin.site.register(Task, TaskAdmin)
admin.site.register(TaskMembership, TaskMembershipAdmin)