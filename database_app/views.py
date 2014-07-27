from django.shortcuts import render
from database_app.models import tmn, Contributions
from django_tables2 import RequestConfig
from database_app.tables import tmntable, ContribTable
from forms import FilterForm


def home(request):
    return render(request, "database_app/home_template.html", {'form': FilterForm()})


def database(request):
    test = ''
    return_queryset = tmn.objects.all()
    try:
        if len(request.GET.getlist('Structure')) > 0:
            return_queryset = return_queryset.filter(Structure__in=request.GET.getlist('Structure'))
    except TypeError:
        pass
    try:
        if len(request.GET.getlist('Metal')) > 0:
            return_queryset = return_queryset.filter(Metal__in=request.GET.getlist('Metal'))
    except TypeError:
        pass

    try:
        if len(request.GET.get('Pughs_ratio_less_than')) > 0:
            return_queryset = return_queryset.filter(k__lt=request.GET.get('Pughs_ratio_less_than'))
    except TypeError:
        pass
    try:
        if len(request.GET.get('Pughs_ratio_greater_than')) > 0:
            return_queryset = return_queryset.filter(k__gt=request.GET.get('Pughs_ratio_greater_than'))
    except TypeError:
        pass

    try:
        if len(request.GET.get('Hardness_less_than')) > 0:
            return_queryset = return_queryset.filter(Vickers_hardness__lt=request.GET.get('Hardness_less_than'))
    except TypeError:
        pass

    try:
        if len(request.GET.get('Hardness_greater_than')) > 0:
            return_queryset = return_queryset.filter(Vickers_hardness__gt=request.GET.get('Hardness_greater_than'))
    except TypeError:
        pass

    try:
        if len(request.GET.get('Lattice_constant_less_than')) > 0:
            return_queryset = return_queryset.filter(Lattice_Constant__lt=request.GET.get('Lattice_constant_less_than'))
    except TypeError:
        pass

    try:
        if len(request.GET.get('Lattice_constant_greater_than')) > 0:
            return_queryset = return_queryset.filter(Lattice_Constant__gt=request.GET.get('Lattice_constant_greater_than'))
    except TypeError:
        pass

    try:
        if len(request.GET.get('Bulk_modulus_less_than')) > 0:
            return_queryset = return_queryset.filter(Bulk_Modulus__lt=request.GET.get('Bulk_modulus_less_than'))
    except TypeError:
        pass

    try:
        if len(request.GET.get('Bulk_modulus_greater_than')) > 0:
            return_queryset = return_queryset.filter(Bulk_Modulus__gt=request.GET.get('Bulk_modulus_greater_than'))
    except TypeError:
        pass

    try:
        if len(request.GET.get('Cauchy_pressure_less_than')) > 0:
            return_queryset = return_queryset.filter(Cauchy_pressure__lt=request.GET.get('Cauchy_pressure_less_than'))
    except TypeError:
        pass

    try:
        if len(request.GET.get('Cauchy_pressure_greater_than')) > 0:
            return_queryset = return_queryset.filter(Cauchy_pressure__gt=request.GET.get('Cauchy_pressure_greater_than'))
    except TypeError:
        pass

    try:
        if len(request.GET.get('Poissons_ratio_less_than')) > 0:
            return_queryset = return_queryset.filter(nu__lt=request.GET.get('Poissons_ratio_less_than'))
    except TypeError:
        pass

    try:
        if len(request.GET.get('Poissons_ratio_greater_than')) > 0:
            return_queryset = return_queryset.filter(nu__gt=request.GET.get('Poissons_ratio_greater_than'))
    except TypeError:
        pass

    try:
        if len(request.GET.get('Experimental')) > 0:
            return_queryset = return_queryset.filter(Experimental=request.GET.get('Experimental'))
    except TypeError:
        pass

    try:
        if len(request.GET.get('Method')) > 0:
            return_queryset = return_queryset.filter(Wave_function__in=request.GET.getlist('Method'))
    except TypeError:
        pass

    try:
        if len(request.GET.get('Potential')) > 0:
            return_queryset = return_queryset.filter(Potential__in=request.GET.getlist('Potential'))
    except TypeError:
        pass

    try:
        if len(request.GET.get('Reference_DOI')) > 0:
            return_queryset = return_queryset.filter(Reference_DOI=request.GET.get('Reference_DOI'))
    except TypeError:
        pass

    try:
        if len(request.GET.get('Stable')) > 0:
            return_queryset = return_queryset.filter(Stable=request.GET.get('Stable'))
    except TypeError:
        pass

    table = tmntable(return_queryset)
    RequestConfig(request).configure(table)
    table.paginate(page=request.GET.get('page', 1), per_page=100)
    return render(request, 'database_app/database_template.html', {'table': table, 'test': test, 'form': FilterForm()})


def document(request):
    return render(request, 'database_app/document_template.html')


def about(request):
    table = ContribTable(Contributions.objects.all())
    table.order_by = 'c_name'
    RequestConfig(request).configure(table)
    table.paginate(page=request.GET.get('page',1), per_page=100)
    return render(request, 'database_app/about_template.html', {'table': table})

