from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, Tab, TabHolder


class FilterForm(forms.Form):

    Structure = forms.MultipleChoiceField(
        choices=(('NbO', 'NbO'), ('zincblende', 'zincblende'), ('rocksalt', 'rocksalt'), ('cesium chloride', 'cesium chloride'), ('anti-ReO3', 'anti-ReO3'), ('bcc','fcc'), ('fluorite','fluorite'), ('pyrite','pyrite'), ('wurtzite','wurtzite')),
    )

    Metal = forms.MultipleChoiceField(
        choices=(('Sc', 'Sc'), ('Ti', 'Ti'), ('V', 'V'), ('Cr', 'Cr'), ('Mn', 'Mn'), ('Fe', 'Fe'), ('Co', 'Co'), ('Ni', 'Ni'), ('Cu', 'Cu'), ('Zn', 'Zn'), ('Y', 'Y'), ('Zr', 'Zr'), ('Nb', 'Nb'), ('Mo', 'Mo'), ('Tc', 'Tc'), ('Ru', 'Ru'), ('Rh', 'Rh'), ('Pd', 'Pd'), ('Ag', 'Ag'), ('Cd', 'Cd'), ('Hf', 'Hf'), ('Ta', 'Ta'), ('W', 'W'), ('Re', 'Re'), ('Os', 'Os'), ('Ir', 'Ir'), ('Pt', 'Pt'), ('Au', 'Au'), ('Hg', 'Hg'), ('Rf', 'Rf'), ('Db', 'Db'), ('Sg', 'Sg'), ('Bh', 'Bh'), ('Hs', 'Hs'), ('Mt', 'Mt'), ('Ds', 'Ds'), ('Rg', 'Rg'), ('Cn', 'Cn')),
    )

    Pughs_ratio_greater_than = forms.FloatField()

    Pughs_ratio_less_than = forms.FloatField()

    Hardness_greater_than = forms.FloatField()

    Hardness_less_than = forms.FloatField()

    Lattice_constant_greater_than = forms.FloatField()

    Lattice_constant_less_than = forms.FloatField()

    Bulk_modulus_less_than = forms.FloatField()

    Bulk_modulus_greater_than = forms.FloatField()

    Poissons_ratio_less_than = forms.FloatField()

    Poissons_ratio_greater_than = forms.FloatField()

    Cauchy_pressure_less_than = forms.FloatField()

    Cauchy_pressure_greater_than = forms.FloatField()

    Reference_DOI = forms.CharField()

    Experimental = forms.BooleanField()

    Stable = forms.BooleanField()

    Method = forms.MultipleChoiceField(
        choices=(('PP', 'PP'), ('PAW', 'PAW'),)
    )

    Potential = forms.MultipleChoiceField(
        choices=(('LDA', 'LDA'), ('GGA', 'GGA'), ('LSDA', 'LSDA'))
    )

    Show_Fields = forms.MultipleChoiceField(
        choices=(('Structure', 'Structure'), ('Metal', 'Metal'), ('Experimental', 'Experimental'), ('Pughs_Ratio', 'Pughs_Ratio'), ('Hardness', 'Hardness'), ('Lattice_Constant', 'Lattice_Constant'), ('Elastic_Constants', 'Elastic_Constants'), ('DOI', 'DOI'),)
    )

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_method = 'get'
    helper.layout = Layout(
        'Structure',
        'Metal',
        'Pughs_ratio_less_than',
        'Pughs_ratio_greater_than',
        'Hardness_less_than',
        'Hardness_greater_than',
        'Lattice_constant_less_than',
        'Lattice_constant_greater_than',
        'Bulk_modulus_less_than',
        'Bulk_modulus_greater_than',
        'Cauchy_pressure_less_than',
        'Cauchy_pressure_greater_than',
        'Poissons_ratio_less_than',
        'Poissons_ratio_greater_than',
        'Experimental',
        'Stable',
        'Method',
        'Potential',
        Field('Reference_DOI', css_class='input-xlarge',),
        'Show_Fields',
        FormActions(
            Submit(type='submit', value='Submit', action='../database/', name='submit', css_class="btn-primary"),
        )
    )
