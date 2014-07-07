from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.core.urlresolvers import reverse_lazy
from database_app.models import tmn
from .filters import ChartFilter
from django_tables2 import RequestConfig

def graph(request):
    import django
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter
    import random
    import datetime

    id_num = HttpRequest["id"]
    queryset_ = tmn.objects.select_related().all()
    response = ChartFilter(request, queryset=queryset_)
    # fig=Figure()
    # ax=fig.add_subplot(111)
    # x=[]
    # y=[]
    # now=datetime.datetime.now()
    # delta=datetime.timedelta(days=1)
    # for i in range(10):
    #     x.append(now)
    #     now+=delta
    #     y.append(random.randint(0, 1000))
    # ax.plot_date(x, y, '-')
    # ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    # fig.autofmt_xdate()
    # canvas=FigureCanvas(fig)
    # response=django.http.HttpResponse(content_type='image/png')
    # canvas.print_png(response)
    return response

def bar(request):
    return render (request, "database_app/submit_form.html")

def element(request):
    return render (request, "database_app/submit_form.html")

def other(request):
    return render (request, "database_app/submit_form.html")