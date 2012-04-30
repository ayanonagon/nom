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
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django import forms
from django.contrib.auth.forms import UserCreationForm

from orders.models import UserProfile, Item, Order
from orders.nomforms import RegistrationForm

from orders.food import Restaurant
from orders.ordrin import *

from collections import defaultdict
from datetime import datetime
from django.utils.timezone import utc
from datetime import timedelta
from random import randint


###############################################

# reverse of login_required.
def logout_required(view):
    def f(request, *args, **kwargs):
        if request.user.is_anonymous():
            return view(request, *args, **kwargs)
        return HttpResponseRedirect('/')
    return f

@login_required
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

@login_required
def openorderlist(request):
    """ return a list of all open orders """
    open_order_list = Order.objects.filter(time_ending__gte=datetime.utcnow().replace(tzinfo=utc))
    paginator = Paginator(open_order_list, 25) # show 25 orders per page
    page = request.GET.get('page')
    try:
        openorders = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        openorders = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        openorders = paginator.page(paginator.num_pages)

    return render_to_response('openorders.html', {"openorders": openorders})

@login_required
def items_in_order(request, order_id):
    """ returns a list of items in the given order """
    selected_order = Order.objects.get(order_id=order_id)

    if request.POST:
        """ adds a user to an order """
        selected_order.joiners.add(request.user.get_profile())

    items_in_order = Item.objects.filter(order=selected_order)

    return render_to_response('order.html', {"items": items_in_order, "order": selected_order})

def nomregister(request):
    if request.user.is_authenticated():
        # They already have an account; don't let them register again
        return render_to_response('register.html', {'has_account': True})

    formdata = RegistrationForm()
    if request.POST:
        new_data = request.POST.copy()
        # Save the profile
        new_user, first_name, phone_number, username, password = formdata.save(new_data)
        new_profile = UserProfile(user=new_user, first_name=first_name, phone_number=phone_number)
        new_profile.save()
        # Login the new user
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully registered!"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your registration details, username, and/or password were incorrect."
        context = {'state': state, 'username': username}
        return render_to_response('auth.html', context)
    else:
        errors = new_data = {}
    
    return render_to_response('register.html', {'form': formdata})

def nomlogin(request):
    """ logs in a user """
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    context = {'state': state, 'username': username}
    return render_to_response('auth.html', context)

@login_required
def nomlogout(request):
    """ logs a user out """
    logout(request)
    return render_to_response('index.html')

@login_required
def nomcreate(request):
    """Create a new order."""
    restaurants = [] #list of restaurants to order from

    #since ordrin only works in a couple of locations (not including Philly),
    #data is pulled from a hardcoded location
    restaurants = get_restaurants('401 Harvey Road', 'College Station', '77840')

    return render_to_response('start_order.html', {"restaurants" : restaurants})

@login_required
def nomsave(request):
    """Saves a new order."""
    if request.POST:
        order_name = request.POST['order_name']
        restaurant = request.POST['from_location']
        owner = request.user.get_profile()
        destination = request.POST['to_location']
        description = request.POST['order_description']
        timeout = int(request.POST['timeout'])
        time_ending = datetime.utcnow().replace(tzinfo=utc) + timedelta(minutes = timeout) 
        order_id = randint(100000, 999999)
        order = Order(name=order_name, restaurant=restaurant, owner=owner, destination=destination, description=description, order_id=order_id, time_ending=time_ending)
        order.save()
    return redirect('/order/' + str(order_id))
