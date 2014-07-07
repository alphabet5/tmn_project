from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tmn_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^database/', include('database_app.urls', namespace='database')),
    url(r'^$', include('database_app.urls', namespace='redirect_database')),
    url(r'^about/$', include('database_app.urls', namespace='about'))
)

#urlpatterns += staticfiles_urlpatterns()