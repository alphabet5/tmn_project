import django_tables2 as tables
from database_app.models import tmn, Contributions


class tmntable(tables.Table):
    # selection = tables.CheckBoxColumn(accessor='pk', orderable=False)
    # id = tables.TemplateColumn('<a href="../detail/{{record.id}}"><b>00{{record.id}}</b></a>', order_by='id')
    # DOI = tables.TemplateColumn('<a href="http://dx.doi.org/{{record.Reference_DOI}}">{{record.Reference_DOI}}</a>', order_by='Reference_DOI')
    # C11_EC = tables.TemplateColumn('{{record.C11_elastic_constant}}', order_by='C11_elastic_constant')
    # C12_EC = tables.TemplateColumn('{{record.C12_elastic_constant}}', order_by='C12_elastic_constant')
    # C44_EC = tables.TemplateColumn('{{record.C44_elastic_constant}}', order_by='C44_elastic_constant')
    # Lattice = tables.TemplateColumn('{{record.Lattice_Constant}}', order_by='Lattice_Constant')
    # Bulk = tables.TemplateColumn('{{record.Bulk_Modulus}}', order_by='Bulk_Modulus')
    # SP = tables.TemplateColumn('{{record.Is_with_spin}}', order_by='Is_with_spin')
    # Exp = tables.TemplateColumn('{{record.Experimental}}', order_by='Experimental')
    # St = tables.TemplateColumn('{{record.Stable}}', order_by='Stable')
    # WF = tables.TemplateColumn('{{record.Wave_function}}', order_by='Wave_function')
    # Code_Pack = tables.TemplateColumn('{{record.Code_Package}}', order_by='Code_Package')
    class Meta:
        model = tmn
        attrs = {"class": "paleblue"}
        exclude = ('Reference_DOI', 'ID', 'Verified', )


class ContribTable(tables.Table):

    class Meta:
        model=Contributions
        fields = ('Name', 'University', 'Contact')
        attrs = {"class": "paleblue"}
