import django_filters
from .models import Procurement

class ProcurementFilter(django_filters.FilterSet):
    reqnumber = django_filters.NumberFilter(field_name='reqnumber', lookup_expr='icontains')
    description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')
    prnumber = django_filters.NumberFilter(field_name='prnumber', lookup_expr='icontains')
    ponumber = django_filters.NumberFilter(field_name='ponumber', lookup_expr='icontains')
    povendor = django_filters.CharFilter(field_name='povendor', lookup_expr='icontains')

    class Meta:
        model = Procurement
        fields = ()
