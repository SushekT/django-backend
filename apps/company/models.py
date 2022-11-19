from django.db import models
from django.core.validators import RegexValidator
from apps.company.constants import TASK_CONDITTON

from apps.core.models import BaseModel, SlugModel
from apps.users.models import User


# Create your models here.
class CompanyBaseModel(BaseModel, SlugModel):
    phone_message = 'Phone number must be entered in the format: 05999999999'
    phone_regex = RegexValidator(
            regex=r'^(977)\d{10}$',
            message=phone_message
        )

    name = models.CharField(max_length=300)
    company_address = models.CharField(max_length=300)
    company_number = models.PositiveBigIntegerField(validators=[phone_regex], null=True, blank=True)
    email_address = models.EmailField(max_length=100)

    def __str__(self):
        return self.name


class Organization(CompanyBaseModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    team = models.ManyToManyField(User, related_name='user', null=True, blank=True)

    def __str__(self)-> str:
        return self.name



class Project(BaseModel, SlugModel):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='organization')
    client = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='client')
    name = models.CharField(max_length=300)
    start_date = models.DateTimeField()
    deadline = models.DateTimeField()
    is_complete = models.BooleanField(default=False)
    price = models.PositiveIntegerField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.name)


class Task(BaseModel, SlugModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=300)
    status = models.CharField(choices=TASK_CONDITTON, default=TASK_CONDITTON[0][1], max_length=100)
    deadline = models.DateTimeField()

    def __str__(self) -> str:
        return str(self.name)