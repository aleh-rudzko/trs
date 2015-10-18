from django.contrib import admin
from tasks.models import Task, TaskMembership


class TaskAdmin(admin.ModelAdmin):
    pass

class TaskMembershipAdmin(admin.ModelAdmin):
    pass

admin.site.register(Task, TaskAdmin)
admin.site.register(TaskMembership, TaskMembershipAdmin)