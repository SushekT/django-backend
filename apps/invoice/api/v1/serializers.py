from rest_framework import serializers
from apps.core.serializers import DynamicFieldsModelSerializer

from apps.invoice.models import InvoiceTemplate


class InvoiceTemplateSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = InvoiceTemplate
        fields = ('template_name', 'profile_logo', 'thumbnail', 'html_template', 'ts_template')