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
    path('edit_procurement/<int:pk>/', views.edit_procurement, name='edit_procurement'),
    path('accounts/', include('django.contrib.auth.urls')),
]
