from django.shortcuts import render, get_object_or_404, redirect
import django_tables2 as tables
from django.views.generic import ListView
from django_filters.views import FilterView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django_tables2 import SingleTableView, RequestConfig, SingleTableMixin
from django.contrib import messages
from tablib import Dataset
from .models import Procurement
from .resources import ProcurementResource
from .tables import ProcurementTable
from .filters import ProcurementFilter
from .forms import ProcurementForm
import pandas as pd
import numpy as np
import requests

def index(request):
    return render(request, 'registration/login.html')

@login_required
def export_data(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        procurement_resource = ProcurementResource()
        dataset = procurement_resource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
            return response

        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="exported_data.json"'
            return response

        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="exported_data.xls"'
            return response

    return render(request, 'datatable/export.html')

@login_required
def import_data(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        procurement_resource = ProcurementResource()
        dataset = Dataset()
        new_procurements = request.FILES['importData']

        if file_format == 'CSV':
            imported_data = dataset.load(new_procurements.read().decode('utf-8'),format='csv')
            # Testing data import
            result = procurement_resource.import_data(dataset, dry_run=True)
        elif file_format == 'JSON':
            imported_data = dataset.load(new_procurements.read().decode('utf-8'),format='json')
            # Testing data import
            result = procurement_resource.import_data(dataset, dry_run=True)

        if not result.has_errors():
            # Import now
            procurement_resource.import_data(dataset, dry_run=False)
            messages.success(request, 'Procurement details updated.')

    return render(request, 'datatable/import.html')

@login_required
def edit_procurement(request, pk):
    procurement = Procurement.objects.get(pk=pk)

    form = ProcurementForm(request.POST or None, instance=procurement)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'datatable/edit_procurement.html', {'form': form, 'procurement': procurement})

class ProcurementListView(SingleTableMixin, FilterView):
    model = Procurement
    table_class = ProcurementTable
    template_name = 'datatable/index.html'
    filterset_class = ProcurementFilter
