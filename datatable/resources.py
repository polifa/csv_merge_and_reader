from import_export import resources
from .models import Procurement

class ProcurementResource(resources.ModelResource):
    class Meta:
        model = Procurement
        exclude = ('id',)
        import_id_field = 'reqnumber'
        import_id_fields = ('reqnumber',)
        fields = ('reqnumber', 'project', "reqcreated", "reqstatus", "description", "prnumber",
         "ponumber", "postatus", "povendor", "pomaterial", "poprice", "pocreated", )
        skip_unchanged = True
        report_skipped = False
        dry_run = True
