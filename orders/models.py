from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class UserProfile(models.Model):
    """A Django model representing a user."""

    phone_number = models.CharField(max_length=11) 
    user = models.OneToOneField(User)
    
    def __unicode__(self):
        return self.phone_number

class Item(models.Model):
    """A Django model representing an item of food or drink ordered by a user."""

    name = models.CharField(max_length=80) # name of the item
    item_id = models.IntegerField() # item id number as stored in Ordr.in's API
    owner = models.ForeignKey(UserProfile, related_name="items_ordered_over_lifetime") # person who ordered this item.

    def __unicode__(self):
        return self.name

class Order(models.Model):
    """A Django model representing a food order."""

    name = models.CharField(max_length=80) # name of the order
    description = models.CharField(max_length=200) # description of the order

    restaurant = models.IntegerField() # restaurant the order is placed at: stored as Ordr.in restaurant id.
    destination = models.CharField(max_length=200) # where user wants order delivered to.
    ordrin_id = models.IntegerField() # order id number as stored in Ordr.in's API.

    items = models.ForeignKey(Item, related_name="associated_order") # the items in the order 

    owner = models.ForeignKey(UserProfile, related_name="started_orders") # The user who started the order.
    joiners = models.ManyToManyField(UserProfile, related_name="joined_orders") # Other users who want in on the order.

    time_created = models.DateTimeField(auto_now_add=True) # time the order was created.
    time_ending = models.DateTimeField() # what time the user is interested in leaving this open until. 

    def __unicode__(self):
        return self.name

