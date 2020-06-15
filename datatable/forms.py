from django import forms
from .models import Procurement

class ProcurementForm(forms.ModelForm):

    class Meta:
        model = Procurement
        fields = ['project']

    def __init__(self, *args, **kwargs):
        super(ProcurementForm, self).__init__(*args, **kwargs)
        self.fields['project'].required = False
