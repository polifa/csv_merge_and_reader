import django_tables2 as tables
from django.utils.html import format_html
from .models import Procurement

class ProcurementTable(tables.Table):
    id = tables.Column(verbose_name='')
    reqnumber = tables.TemplateColumn("<a href='https://eccprd.corp.amdocs.com/irj/portal/P2P?NavMode=10&req={{record.reqnumber}}'>{{record.reqnumber}}</a>")
    prnumber = tables.TemplateColumn("""
    {% if record.prnumber != '0' %}
    <a href='https://eccprd.corp.amdocs.com/irj/portal/P2P?NavMode=10&pr={{record.prnumber}}'>{{record.prnumber}}</a>
    {% endif %}
    {% if record.prnumber == '0' %}
    <a>--</a>
    {% endif %}
    """)
    ponumber = tables.TemplateColumn("""
    {% if record.ponumber != '0' %}
    <a href='https://eccprd.corp.amdocs.com/irj/portal/P2P?NavMode=10&po={{record.ponumber}}'>{{record.ponumber}}</a>
    {% endif %}
    {% if record.ponumber == '0' %}
    <a>--</a>
    {% endif %}
    """)

    def render_id(self, value):
        return format_html('<input type="hidden" name="track_id" value="{}" />', str(value))

    class Meta:
        model = Procurement
        template_name = "django_tables2/bootstrap4.html"
