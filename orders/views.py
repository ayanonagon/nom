from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpRequest
from django.template.loader import get_template
from django.template import Context, RequestContext, TemplateDoesNotExist
from django.shortcuts import render_to_response, redirect
from django.views.generic.simple import direct_to_template
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Caching
from django.views.decorators.cache import never_cache
from django.core.cache import cache
from django.utils.cache import get_cache_key

from django import http

from django.contrib.auth.models import User
from orders.models import UserProfile, Item, Order

from collections import defaultdict

###############################################

#def login(request):    
    #email = request.POST['email']
    #password = request.POST['password']

def userlist(request):
    """ return a list of userprofiles """
    user_list = UserProfile.objects.all()
    paginator = Paginator(user_list, 25) # show 25 contacts per page
    
    page = request.GET.get('page')
    try:
        userprofiles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        userprofiles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        userprofiles = paginator.page(paginator.num_pages)
    
    return render_to_response('userlist.html', {"userprofiles": userprofiles})

def index(request):
    return render_to_response('index.html')


