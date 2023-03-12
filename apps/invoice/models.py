from django.db import models

from apps.company.models import Project
from apps.core.models import BaseModel, SlugModel
from apps.users.models import User


# Create your models here.
class MainInvoice(BaseModel, SlugModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    reg_number = models.BigIntegerField(null=True, blank=True)
    paid = models.BooleanField(default=False)

    @property
    def total(self):
        return sum(task.sub_total for task in self.main_invoice.all()) if self.main_invoice.all().exist() else 0


class SubInvoice(models.Model):
    main_invoice = models.ForeignKey(MainInvoice, on_delete=models.CASCADE, related_name='main_invoice')
    description = models.TextField(null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True)
    sub_total = models.BigIntegerField(null=True, blank=True)



class InvoiceTemplate(BaseModel):
    template_name = models.CharField(max_length=256)
    profile_logo = models.ImageField(upload_to='profile/')
    thumbnail = models.ImageField(upload_to='thumbnail/')
    data = models.JSONField(default=dict)
    html_template = models.TextField()
    ts_template = models.TextField()
    is_archived = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.template_name

    
