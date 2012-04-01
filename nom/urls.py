from django.conf.urls import patterns, include, url
from django_twilio.views import sms

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nom.views.home', name='home'),
    # url(r'^nom/', include('nom.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # Twilio SMS reply
    url(r'^sms/$', 'django_twilio.views.sms', {
        'message': 'Thanks for the SMS. Talk to you soon!',
    }),
)
