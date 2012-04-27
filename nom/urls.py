from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template, redirect_to
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from orders.views import userlist

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    
    url('^index/$', direct_to_template, {'template': 'index.html'}),

    url('^users/$', userlist, name='userlist'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
) 
