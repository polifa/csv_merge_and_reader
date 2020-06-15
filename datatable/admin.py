from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib import admin
from django.utils.html import format_html
from .models import Procurement, Project
from .resources import ProcurementResource

class ProcurementAdmin(ImportExportModelAdmin):
    resource_class = ProcurementResource
    list_per_page = 15
    list_display_links = None

    def change_button(self, obj):
        return format_html('<a class="btn" href="/admin/datatable/procurement/{}/change/">Edit</a>', obj.id)

    def change_view(self, request, object_id, extra_context=None):
        self.exclude = ('reqnumber','reqstatus','description','prnumber','ponumber','reqcreated','povendor','postatus','pomaterial','poprice','pocreated')
        return super().change_view(request, object_id, extra_context)

    list_display = ("reqnumber","project", "reqcreated", "reqstatus", "description", "prnumber",
     "ponumber", "postatus", "povendor", "pomaterial", "poprice", "pocreated", "change_button")

admin.site.register(Procurement, ProcurementAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('projectname',)

admin.site.register(Project, ProjectAdmin)
admin.site.site_url = "/datatable"
