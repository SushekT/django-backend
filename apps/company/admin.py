from django.contrib import admin

from apps.company.models import Organization, Project, Task

# Register your models here.

class OrganizationAdmin(admin.ModelAdmin):
    search_fields = ('owner__name', 'owner__company_number')


admin.site.register(Organization, OrganizationAdmin)



class ProjectAdmin(admin.ModelAdmin):
    search_fields = ('name', 'organization')


admin.site.register(Project, ProjectAdmin)

class TaskAdmin(admin.ModelAdmin):
    search_fields = ('task_name', 'project')


admin.site.register(Task, TaskAdmin)