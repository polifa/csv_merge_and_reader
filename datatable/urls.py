from django.urls import path
from django_filters.views import FilterView
from django.conf.urls import include
from django.contrib import auth
from django.contrib import admin
from . import views
from .views import ProcurementListView


urlpatterns = [
    path('', ProcurementListView.as_view(), name="index"),
    path('import/', views.import_data, name='import_data'),
    path('export/', views.export_data, name='export_data'),
    path('merge_csv_files/', views.merge_csv_files, name='merge_csv_files'),
    path('accounts/', include('django.contrib.auth.urls')),
]
