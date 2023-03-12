from django.urls import path, include

app_name = "api_v1"

urlpatterns = [
    path('user/', include('apps.users.api.v1.urls.users', namespace='users')),
    path('invoice/template/', include('apps.invoice.api.v1.urls.templates', namespace='invoice_templates'))
]
