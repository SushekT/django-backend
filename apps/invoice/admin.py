from django.contrib import admin

from apps.invoice.models import InvoiceTemplate

# Register your models here.


class InvoiceTemplateAdmin(admin.ModelAdmin):
    search_fields = ('task_name', 'project')


admin.site.register(InvoiceTemplate, InvoiceTemplateAdmin)