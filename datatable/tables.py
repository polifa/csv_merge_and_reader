import django_tables2 as tables
from django.utils.html import format_html
from .models import Procurement
from django_tables2.utils import A


class ProcurementTable(tables.Table):
    id = tables.Column(verbose_name='')
    actions = tables.LinkColumn('edit_procurement', args=[A('pk')], verbose_name='Actions', empty_values=(), text='Edit')
    reqnumber = tables.TemplateColumn("<a href='https://eccprd.corp.amdocs.com/irj/portal/P2P?NavMode=10&req={{record.reqnumber}}' target='_blank'>{{record.reqnumber}}</a>")

    prnumber = tables.TemplateColumn("""
    {% if record.prnumber != '0' %}
    <a href='https://eccprd.corp.amdocs.com/irj/portal/P2P?NavMode=10&pr={{record.prnumber}}' target='_blank'>{{record.prnumber}}</a>
    {% endif %}
    {% if record.prnumber == '0' %}
    <a>__</a>
    {% endif %}
    """)

    ponumber = tables.TemplateColumn("""
    {% if record.ponumber != '0' %}
    <a href='https://eccprd.corp.amdocs.com/irj/portal/P2P?NavMode=10&po={{record.ponumber}}' target='_blank'>{{record.ponumber}}</a>
    {% endif %}
    {% if record.ponumber == '0' %}
    <a>__</a>
    {% endif %}
    """)

    def render_id(self, value):
        return format_html('<input type="hidden" name="track_id" value="{}" />', str(value))

    def before_render(self, request):
        if request.user.has_perm('datatable.change_datatable'):
            self.columns.show('actions')
        else:
            self.columns.hide('actions')

    class Meta:
        model = Procurement
        template_name = "django_tables2/bootstrap4.html"
        order_by = '-reqnumber'
