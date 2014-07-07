from django.conf.urls import patterns, url
from database_app import views
from django.conf import settings
from django.conf.urls.static import static

from django_filters.views import FilterView
from database_app.models import tmn

urlpatterns = patterns('',
                       url(r'^$', views.about, name='about'),
                       url(r'^index/$', views.search_filter, name="search_filter"),
                       url(r'^detail/(?P<pk>\d+)', views.Detail.as_view(), name="detail_view"),
                       url(r'^charts/$', views.charts, name="charts"),
                       url(r'^filter/$', views.admin_filter, name='admin_filter'),
                       url(r'^charts/graph.png$', 'database_app.charts.graph', name='graph'),
                       url(r'^charts/bar.png$', 'database_app.charts.bar', name='bar'),
                       url(r'^charts/element.png$', 'database_app.charts.element', name='element'),
                       url(r'^charts/other.png$', 'database_app.charts.other', name='other'),
                       url(r'^selection/tmn_database.csv$', views.csv_selection, name='csv_selection'),
                       url(r'^all/tmn_database.csv$', views.csv_all, name='csv_all'),
                      ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
