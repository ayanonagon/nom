from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class UserProfile(models.Model):
    """A Django model representing a user."""

    first_name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=11) 
    user = models.OneToOneField(User)
    
    def __unicode__(self):
        return self.phone_number

class Order(models.Model):
    """A Django model representing a food order."""

    order_id = models.IntegerField() # an integer id number used to represent the order in our app
    name = models.CharField(max_length=80) # name of the order
    description = models.CharField(max_length=200) # description of the order

    restaurant = models.CharField(max_length=80) # restaurant the order is placed at
    rid = models.IntegerField() #restaurant ID (based on the ordrin API)
    destination = models.CharField(max_length=200) # where user wants order delivered to.

    owner = models.ForeignKey(UserProfile, related_name="started_orders") # The user who started the order.
    joiners = models.ManyToManyField(UserProfile, related_name="joined_orders") # Other users who want in on the order.

    time_created = models.DateTimeField(auto_now_add=True) # time the order was created.
    time_ending = models.DateTimeField() # what time the user is interested in leaving this open until. 

    def __unicode__(self):
        return self.name

class Item(models.Model):
    """A Django model representing an item of food or drink ordered by a user."""

    name = models.CharField(max_length=80) # name of the item

    owner = models.ForeignKey(UserProfile, related_name="items_ordered_over_lifetime") # person who ordered this item.
    order = models.ForeignKey(Order, related_name="items_in_the_order") # the order which the item is in

    def __unicode__(self):
        return self.name

