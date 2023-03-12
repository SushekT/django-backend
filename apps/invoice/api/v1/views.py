from apps.core.viewsets import ListRetrieveUpdateViewSet
from apps.invoice.api.v1.serializers import InvoiceTemplateSerializer

from apps.invoice.models import InvoiceTemplate


class InvoiceTemplateListRetrieve(ListRetrieveUpdateViewSet):
    queryset = InvoiceTemplate.objects.all()
    serializer_class = InvoiceTemplateSerializer