import django_filters
from database_app.models import tmn


class IndexFilter(django_filters.FilterSet):

    class Meta:
        model = tmn
        fields = ['Structure', 'Metal', 'Lattice_Constant', 'Bulk_Modulus', 'C11_elastic_constant', 'C12_elastic_constant', 'C44_elastic_constant', 'Experimental', 'Stable', 'Is_with_spin', 'Potential', 'Wave_function', 'Code_Package', 'Reference_DOI', 'Verified']


class ChartFilter(django_filters.FilterSet):

    class Meta:
        model = tmn
        fields = ['Structure', 'Metal', 'Lattice_Constant', 'Bulk_Modulus', 'C11_elastic_constant', 'C12_elastic_constant', 'C44_elastic_constant', 'Experimental', 'Stable', 'Is_with_spin', 'Potential', 'Wave_function', 'Code_Package', 'Reference_DOI', 'Verified']
