from import_export import resources
from .models import Procurement

class ProcurementResource(resources.ModelResource):
    class Meta:
        model = Procurement
