from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpRequest
from django.template.loader import get_template
from django.template import Context, RequestContext, TemplateDoesNotExist
from django.shortcuts import render_to_response, redirect
from django.views.generic.simple import direct_to_template
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.context_processors import csrf

# Caching
from django.views.decorators.cache import never_cache
from django.core.cache import cache
from django.utils.cache import get_cache_key

from django import http

from django.contrib.auth.models import User
from orders.models import UserProfile, Item, Order

from collections import defaultdict

###############################################

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

def items_in_order(request, order_id):
    """ returns a list of items in the given order """
    selected_order = Order.objects.get(order_id=order_id)
    items_in_order = Item.objects.filter(order=selected_order)

    return render_to_response('order.html', {"items": items_in_order, "order": selected_order})

def login(request):
    """ logs in a user """

def logout(request):
    """ logs a user out """
