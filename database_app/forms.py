from database_app.models import *
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class StructureForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(StructureForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))

    class Meta:
        model = tmn


class StructureUpdateForm(StructureForm):

    class Meta:
        model = tmn
#        fields = ['Structure', 'Metal']