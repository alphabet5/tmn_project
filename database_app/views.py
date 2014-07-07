from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from database_app.models import tmn
from .filters import IndexFilter, ChartFilter
from django_tables2 import RequestConfig
from database_app.tables import tmntable
from django.views.generic import FormView, CreateView, UpdateView, DeleteView, DetailView
from forms import *

#from django.template import RequestContext, loader
#from django.core.urlresolvers import reverse
#from django.views.generic import ListView
import django_filters


# Create your views here.


def about(request):
    return render(request, "database_app/about.html")

def charts(request):
    queryset_ = tmn.objects.select_related().all()
    f = ChartFilter(request.GET, queryset=queryset_)
    table = tmntable(f.qs)
    RequestConfig(request).configure(table)
    table.paginate(page=request.GET.get('page', 1), per_page=100)
    image = HttpResponse("%s" % request.GET)
    return render(request, 'database_app/charts.html', {'filter': f, 'table': table, 'image': image})

def search_filter(request):
    queryset_ = tmn.objects.select_related().all()
    f = IndexFilter(request.GET, queryset=queryset_)
    table = tmntable(f.qs)
    RequestConfig(request).configure(table)
    table.paginate(page=request.GET.get('page', 1), per_page=100)
    return render(request, 'database_app/search_filter.html', {'table': table, 'filter': f})


class Detail(DetailView):
    model = tmn
    template_name = 'database_app/detail_view.html'


def admin_filter(request):
    queryset_ = tmn.objects.select_related().all()
    f = IndexFilter(request.GET, queryset=queryset_)
    table = tmntable(f.qs)
    RequestConfig(request).configure(table)
    table.paginate(page=request.GET.get('page', 1), per_page=1000)
    return render(request, 'database_app/admin_filter.html', {'table': table , 'filter' : f})


def csv_all(request):
    x = ""
    for item in tmn.objects.all():
        x += str(item.pk)+str(item.Bulk_Modulus)+str(item.Code_Package)+'<br>'
    response=HttpResponse(x)
#    t = tmn.objects.all()
    return response #render(request, "database_app/about.html", {'table': t})

def csv_selection(request):
    x = ""
    for item in tmn.objects.all():
        x += str(item.pk)+str(item.Bulk_Modulus)+str(item.Code_Package)+'<br>'
    response=HttpResponse(x)
#    t = tmn.objects.all()
    return response #render(request, "database_app/about.html", {'table': t})
