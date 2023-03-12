from django.urls import path
from rest_framework import routers

from apps.invoice.api.v1.views import InvoiceTemplateListRetrieve

app_name = 'invoice_templates'

router = routers.DefaultRouter()
router.register(r'', InvoiceTemplateListRetrieve, basename='invoice_template')


urlpatterns = [
]

urlpatterns += router.urls