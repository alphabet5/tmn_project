from django.conf.urls import patterns, url
from database_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
                       url(r'^$', views.about, name='about'),
                       url(r'^home/$', views.home, name='home'),
                       url(r'^database/$', views.database, name='database'),
                       url(r'^document/$', views.document, name='document'),
                       url(r'^about/$', views.about, name='about'),
                       ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
