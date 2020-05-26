from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib import admin
from django.utils.html import format_html
from .models import Procurement
from .resources import ProcurementResource

class ProcurementAdmin(ImportExportModelAdmin):
    resource_class = ProcurementResource
    list_per_page = 15
    list_display_links = None

    def change_button(self, obj):
        return format_html('<a class="btn" href="/admin/datatable/procurement/{}/change/">Edit</a>', obj.id)

    list_display = ("reqnumber", "reqcreated", "reqstatus", "description", "prnumber",
     "ponumber", "postatus", "povendor", "pomaterial", "poprice", "pocreated", "change_button")

admin.site.register(Procurement, ProcurementAdmin)
admin.site.site_url = "/datatable"
