import django_filters
from .models import Procurement
from django.forms.widgets import TextInput

class ProcurementFilter(django_filters.FilterSet):
    reqnumber = django_filters.NumberFilter(field_name='reqnumber', lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'REQ Number...'}))
    description = django_filters.CharFilter(field_name='description', lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'Description...'}))
    prnumber = django_filters.NumberFilter(field_name='prnumber', lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'PR Number...'}))
    ponumber = django_filters.NumberFilter(field_name='ponumber', lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'PO Number...'}))
    povendor = django_filters.CharFilter(field_name='povendor', lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'PO Vendor...'}))

    class Meta:
        model = Procurement
        fields = ()
