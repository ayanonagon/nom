from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template, redirect_to
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from orders.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    
    url('^users/$', userlist),

    url('^order/(?P<order_id>\d{6})/$', items_in_order),

    # dealing with logins
    url(r'^login/$', logout_required(nomlogin)),
    url(r'^logout/$', nomlogout),
    url(r'^register/$', logout_required(nomregister)),
    url(r'^start_order/$', nomcreate),
    url(r'^save_order/$', nomsave),
    url('^$', direct_to_template, {'template': 'index.html'}),
 
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
) 
